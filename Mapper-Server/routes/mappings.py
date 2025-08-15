from flask import Blueprint, request, jsonify
from database.models import db, Mapping, User
from datetime import datetime, timezone

mappings_bp = Blueprint('mappings', __name__, url_prefix='/api/mappings')

@mappings_bp.route('/', methods=['GET'])
def get_mappings():
    """Retorna todos os mapeamentos"""
    try:
        mappings = Mapping.query.all()
        return jsonify({
            'success': True,
            'data': [mapping.to_dict() for mapping in mappings],
            'count': len(mappings)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@mappings_bp.route('/<int:mapping_id>', methods=['GET'])
def get_mapping(mapping_id):
    """Retorna um mapeamento específico"""
    try:
        mapping = db.session.get(Mapping, mapping_id)
        if not mapping:
            return jsonify({
                'success': False,
                'error': 'Mapeamento não encontrado'
            }), 404
        return jsonify({
            'success': True,
            'data': mapping.to_dict()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@mappings_bp.route('/', methods=['POST'])
def create_mapping():
    """Cria um novo mapeamento"""
    try:
        data = request.get_json()
        
        if not data or not data.get('name') or not data.get('created_by'):
            return jsonify({
                'success': False,
                'error': 'Nome e created_by são obrigatórios'
            }), 400
        
        # Verifica se o usuário existe
        user = db.session.get(User, data['created_by'])
        if not user:
            return jsonify({
                'success': False,
                'error': 'Usuário não encontrado'
            }), 404
        
        new_mapping = Mapping(
            name=data['name'],
            description=data.get('description', ''),
            source_data=data.get('source_data', {}),
            target_schema=data.get('target_schema', {}),
            created_by=data['created_by']
        )
        
        db.session.add(new_mapping)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': new_mapping.to_dict(),
            'message': 'Mapeamento criado com sucesso'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@mappings_bp.route('/<int:mapping_id>', methods=['PUT'])
def update_mapping(mapping_id):
    """Atualiza um mapeamento existente"""
    try:
        mapping = db.session.get(Mapping, mapping_id)
        if not mapping:
            return jsonify({
                'success': False,
                'error': 'Mapeamento não encontrado'
            }), 404
        data = request.get_json()
        
        if data.get('name'):
            mapping.name = data['name']
        if data.get('description') is not None:
            mapping.description = data['description']
        if data.get('source_data') is not None:
            mapping.source_data = data['source_data']
        if data.get('target_schema') is not None:
            mapping.target_schema = data['target_schema']
        
        mapping.updated_at = datetime.now(timezone.utc)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': mapping.to_dict(),
            'message': 'Mapeamento atualizado com sucesso'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@mappings_bp.route('/<int:mapping_id>', methods=['DELETE'])
def delete_mapping(mapping_id):
    """Remove um mapeamento"""
    try:
        mapping = db.session.get(Mapping, mapping_id)
        if not mapping:
            return jsonify({
                'success': False,
                'error': 'Mapeamento não encontrado'
            }), 404
        db.session.delete(mapping)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Mapeamento removido com sucesso'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@mappings_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_mappings(user_id):
    """Retorna todos os mapeamentos de um usuário específico"""
    try:
        user = db.session.get(User, user_id)
        if not user:
            return jsonify({
                'success': False,
                'error': 'Usuário não encontrado'
            }), 404
        mappings = Mapping.query.filter_by(created_by=user_id).all()
        
        return jsonify({
            'success': True,
            'data': [mapping.to_dict() for mapping in mappings],
            'count': len(mappings),
            'user': user.username
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

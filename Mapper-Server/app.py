from flask import Flask, jsonify
from flask_cors import CORS
import os
from config import config
from database.database import init_db
from routes.users import users_bp
from routes.mappings import mappings_bp

def create_app(config_name=None):
    """Factory function para criar a aplicação Flask"""
    
    # Determina qual configuração usar
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    
    # Carrega a configuração
    app.config.from_object(config[config_name])
    
    # Inicializa CORS
    CORS(app)
    
    # Inicializa o banco de dados
    init_db(app)
    
    # Registra os blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(mappings_bp)
    
    # Rota de health check
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'Mapper-Server',
            'version': '1.0.0'
        })
    
    # Rota raiz
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({
            'message': 'Bem-vindo ao Mapper-Server API',
            'version': '1.0.0',
            'endpoints': {
                'users': '/api/users',
                'mappings': '/api/mappings',
                'health': '/health'
            }
        })
    
    # Handler para erros 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 'Endpoint não encontrado'
        }), 404
    
    # Handler para erros 500
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 'Erro interno do servidor'
        }), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=app.config.get('DEBUG', False)
    )

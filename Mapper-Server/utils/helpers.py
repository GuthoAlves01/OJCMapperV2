import json
from datetime import datetime
from typing import Any, Dict, List

def validate_json_schema(data: Any, schema: Dict) -> bool:
    """
    Valida se os dados seguem o schema especificado
    
    Args:
        data: Dados a serem validados
        schema: Schema de validação
        
    Returns:
        bool: True se válido, False caso contrário
    """
    try:
        if not isinstance(schema, dict):
            return False
            
        if schema.get('type') == 'object':
            if not isinstance(data, dict):
                return False
                
            required_fields = schema.get('required', [])
            for field in required_fields:
                if field not in data:
                    return False
                    
            properties = schema.get('properties', {})
            for field, value in data.items():
                if field in properties:
                    field_schema = properties[field]
                    if not validate_json_schema(value, field_schema):
                        return False
                        
        elif schema.get('type') == 'array':
            if not isinstance(data, list):
                return False
                
            items_schema = schema.get('items')
            if items_schema:
                for item in data:
                    if not validate_json_schema(item, items_schema):
                        return False
                        
        elif schema.get('type') == 'string':
            if not isinstance(data, str):
                return False
                
        elif schema.get('type') == 'number':
            if not isinstance(data, (int, float)):
                return False
                
        elif schema.get('type') == 'integer':
            if not isinstance(data, int):
                return False
                
        elif schema.get('type') == 'boolean':
            if not isinstance(data, bool):
                return False
                
        return True
        
    except Exception:
        return False

def format_datetime(dt: datetime) -> str:
    """Formata datetime para string ISO"""
    if dt:
        return dt.isoformat()
    return None

def parse_datetime(dt_str: str) -> datetime:
    """Converte string ISO para datetime"""
    try:
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except:
        return None

def sanitize_input(data: str) -> str:
    """Remove caracteres perigosos da entrada"""
    if not data:
        return data
    
    dangerous_chars = ['<', '>', '"', "'", '&']
    for char in dangerous_chars:
        data = data.replace(char, '')
    
    return data.strip()

def create_response(success: bool, data: Any = None, message: str = None, error: str = None) -> Dict:
    """Cria uma resposta padronizada da API"""
    response = {
        'success': success,
        'timestamp': datetime.utcnow().isoformat()
    }
    
    if data is not None:
        response['data'] = data
        
    if message:
        response['message'] = message
        
    if error:
        response['error'] = error
        
    return response

def paginate_results(query, page: int = 1, per_page: int = 10) -> Dict:
    """Pagina os resultados de uma query"""
    pagination = query.paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    
    return {
        'items': [item.to_dict() for item in pagination.items],
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': pagination.total,
            'pages': pagination.pages,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev
        }
    }

import pytest
import json
from app import create_app
from database.models import db, User, Mapping

@pytest.fixture
def app():
    """Cria uma instância da aplicação para testes"""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """Cliente de teste"""
    return app.test_client()

@pytest.fixture
def sample_user():
    """Usuário de exemplo para testes"""
    return {
        'username': 'testuser',
        'email': 'test@example.com'
    }

@pytest.fixture
def sample_mapping():
    """Mapeamento de exemplo para testes"""
    return {
        'name': 'Test Mapping',
        'description': 'Test description',
        'source_data': {'field1': 'value1'},
        'target_schema': {'field1': 'string'},
        'created_by': 1
    }

def test_create_mapping(client, sample_user, sample_mapping):
    """Testa criação de mapeamento"""
    # Cria um usuário primeiro
    client.post('/api/users/',
                data=json.dumps(sample_user),
                content_type='application/json')
    
    # Cria um mapeamento
    response = client.post('/api/mappings/',
                          data=json.dumps(sample_mapping),
                          content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['name'] == sample_mapping['name']
    assert data['data']['description'] == sample_mapping['description']

def test_get_mappings(client, sample_user, sample_mapping):
    """Testa listagem de mapeamentos"""
    # Cria um usuário
    client.post('/api/users/',
                data=json.dumps(sample_user),
                content_type='application/json')
    
    # Cria um mapeamento
    client.post('/api/mappings/',
                data=json.dumps(sample_mapping),
                content_type='application/json')
    
    # Busca todos os mapeamentos
    response = client.get('/api/mappings/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['success'] is True
    assert len(data['data']) == 1
    assert data['count'] == 1

def test_get_mapping(client, sample_user, sample_mapping):
    """Testa busca de mapeamento específico"""
    # Cria um usuário
    client.post('/api/users/',
                data=json.dumps(sample_user),
                content_type='application/json')
    
    # Cria um mapeamento
    create_response = client.post('/api/mappings/',
                                 data=json.dumps(sample_mapping),
                                 content_type='application/json')
    mapping_id = json.loads(create_response.data)['data']['id']
    
    # Busca o mapeamento criado
    response = client.get(f'/api/mappings/{mapping_id}')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['id'] == mapping_id

def test_update_mapping(client, sample_user, sample_mapping):
    """Testa atualização de mapeamento"""
    # Cria um usuário
    client.post('/api/users/',
                data=json.dumps(sample_user),
                content_type='application/json')
    
    # Cria um mapeamento
    create_response = client.post('/api/mappings/',
                                 data=json.dumps(sample_mapping),
                                 content_type='application/json')
    mapping_id = json.loads(create_response.data)['data']['id']
    
    # Atualiza o mapeamento
    update_data = {'name': 'Updated Mapping'}
    response = client.put(f'/api/mappings/{mapping_id}',
                          data=json.dumps(update_data),
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['name'] == 'Updated Mapping'

def test_delete_mapping(client, sample_user, sample_mapping):
    """Testa remoção de mapeamento"""
    # Cria um usuário
    client.post('/api/users/',
                data=json.dumps(sample_user),
                content_type='application/json')
    
    # Cria um mapeamento
    create_response = client.post('/api/mappings/',
                                 data=json.dumps(sample_mapping),
                                 content_type='application/json')
    mapping_id = json.loads(create_response.data)['data']['id']
    
    # Remove o mapeamento
    response = client.delete(f'/api/mappings/{mapping_id}')
    assert response.status_code == 200
    
    # Verifica se foi removido
    get_response = client.get(f'/api/mappings/{mapping_id}')
    assert get_response.status_code == 404

def test_get_user_mappings(client, sample_user, sample_mapping):
    """Testa busca de mapeamentos de um usuário específico"""
    # Cria um usuário
    client.post('/api/users/',
                data=json.dumps(sample_user),
                content_type='application/json')
    
    # Cria um mapeamento
    client.post('/api/mappings/',
                data=json.dumps(sample_mapping),
                content_type='application/json')
    
    # Busca mapeamentos do usuário
    response = client.get('/api/mappings/user/1')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['success'] is True
    assert len(data['data']) == 1
    assert data['user'] == 'testuser'

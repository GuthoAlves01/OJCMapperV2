import pytest
import json
from app import create_app
from database.models import db, User

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

def test_create_user(client, sample_user):
    """Testa criação de usuário"""
    response = client.post('/api/users/',
                          data=json.dumps(sample_user),
                          content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['username'] == sample_user['username']
    assert data['data']['email'] == sample_user['email']

def test_get_users(client, sample_user):
    """Testa listagem de usuários"""
    # Cria um usuário primeiro
    client.post('/api/users/',
                data=json.dumps(sample_user),
                content_type='application/json')
    
    # Busca todos os usuários
    response = client.get('/api/users/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['success'] is True
    assert len(data['data']) == 1
    assert data['count'] == 1

def test_get_user(client, sample_user):
    """Testa busca de usuário específico"""
    # Cria um usuário
    create_response = client.post('/api/users/',
                                 data=json.dumps(sample_user),
                                 content_type='application/json')
    user_id = json.loads(create_response.data)['data']['id']
    
    # Busca o usuário criado
    response = client.get(f'/api/users/{user_id}')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['id'] == user_id

def test_update_user(client, sample_user):
    """Testa atualização de usuário"""
    # Cria um usuário
    create_response = client.post('/api/users/',
                                 data=json.dumps(sample_user),
                                 content_type='application/json')
    user_id = json.loads(create_response.data)['data']['id']
    
    # Atualiza o usuário
    update_data = {'username': 'updateduser'}
    response = client.put(f'/api/users/{user_id}',
                          data=json.dumps(update_data),
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['username'] == 'updateduser'

def test_delete_user(client, sample_user):
    """Testa remoção de usuário"""
    # Cria um usuário
    create_response = client.post('/api/users/',
                                 data=json.dumps(sample_user),
                                 content_type='application/json')
    user_id = json.loads(create_response.data)['data']['id']
    
    # Remove o usuário
    response = client.delete(f'/api/users/{user_id}')
    assert response.status_code == 200
    
    # Verifica se foi removido
    get_response = client.get(f'/api/users/{user_id}')
    assert get_response.status_code == 404

import os
import json
from pathlib import Path

# Configurações padrão
DEFAULT_CONFIG = {
    'api_url': 'http://localhost:5000/api',
    'auth_token': None,
    'current_user': None,
    'last_project': None,
    'theme': 'light'
}

CONFIG_FILE = Path.home() / '.mapper_client_config.json'

# Carrega ou cria configuração
if CONFIG_FILE.exists():
    with open(CONFIG_FILE, 'r') as f:
        APP_CONFIG = {**DEFAULT_CONFIG, **json.load(f)}
else:
    APP_CONFIG = DEFAULT_CONFIG
    with open(CONFIG_FILE, 'w') as f:
        json.dump(APP_CONFIG, f)

def save_config():
    """Salva a configuração atual no arquivo"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(APP_CONFIG, f)
#!/usr/bin/env python3
"""
Script para executar a aplicação Mapper-Server
"""

import os
from app import create_app

if __name__ == '__main__':
    # Carrega variáveis de ambiente do arquivo .env se existir
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_file):
        from dotenv import load_dotenv
        load_dotenv(env_file)
    
    # Cria e executa a aplicação
    app = create_app()
    
    # Configurações de execução
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print(f"🚀 Iniciando Mapper-Server em http://{host}:{port}")
    print(f"📊 Ambiente: {os.environ.get('FLASK_ENV', 'development')}")
    print(f"🐛 Debug: {debug}")
    
    app.run(
        host=host,
        port=port,
        debug=debug
    )

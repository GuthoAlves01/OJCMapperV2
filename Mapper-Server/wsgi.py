#!/usr/bin/env python3
"""
WSGI entry point para deploy em produção
"""

import os
from app import create_app

# Cria a aplicação Flask
app = create_app(os.environ.get('FLASK_ENV', 'production'))

if __name__ == '__main__':
    app.run()

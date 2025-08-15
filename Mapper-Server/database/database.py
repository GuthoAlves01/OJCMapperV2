from flask_migrate import Migrate
from .models import db

migrate = Migrate()

def init_db(app):
    """Inicializa o banco de dados"""
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        db.create_all()
        
def get_db():
    """Retorna a instância do banco de dados"""
    return db

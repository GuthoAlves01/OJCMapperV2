# 🗺️ Mapper-Server

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)](https://www.sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-lightgrey.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-11%20passed-brightgreen.svg)](tests/)

> **API REST robusta para gerenciamento de mapeamentos de dados, construída com as melhores práticas de desenvolvimento Python.**

## ✨ Características

- 🚀 **API RESTful** com endpoints para usuários e mapeamentos
- 🗄️ **Banco de dados SQLite** com SQLAlchemy ORM
- 🏗️ **Arquitetura modular** com blueprints Flask
- ✅ **Validação de dados** e tratamento de erros robusto
- 🧪 **Testes automatizados** com pytest (100% passando)
- 🌐 **CORS habilitado** para integração com aplicações cliente
- ⚙️ **Configurações por ambiente** (dev, prod, test)
- 📊 **Documentação completa** da API
- 🔒 **Tratamento de segurança** e sanitização de dados

## 🛠️ Stack Tecnológica

### **Backend**
- **Python 3.8+** - Linguagem principal
- **Flask 2.3.3** - Framework web
- **SQLAlchemy 2.0+** - ORM para banco de dados
- **SQLite** - Banco de dados relacional
- **Flask-Migrate** - Sistema de migrações
- **Flask-CORS** - Suporte a CORS

### **Desenvolvimento & Testes**
- **pytest** - Framework de testes
- **pytest-flask** - Extensões para testes Flask
- **python-dotenv** - Gerenciamento de variáveis de ambiente

### **Arquitetura**
- **Factory Pattern** - Criação de aplicação
- **Blueprint Pattern** - Organização de rotas
- **Repository Pattern** - Acesso a dados
- **Error Handling** - Tratamento centralizado de erros

## 📋 Pré-requisitos

- **Python 3.8+** (recomendado: Python 3.11+)
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)

## 🚀 Início Rápido

### 1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd Mapper-Server
```

### 2. **Configure o ambiente virtual**
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### 4. **Configure as variáveis de ambiente**
```bash
# Copie o arquivo de exemplo
copy env.example .env

# Edite o arquivo .env com suas configurações
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///mapper.db
PORT=5000
HOST=0.0.0.0
DEBUG=True
```

### 5. **Execute a aplicação**
```bash
# Opção 1: Script personalizado (recomendado)
python run.py

# Opção 2: Aplicação principal
python app.py

# Opção 3: Flask CLI
flask run
```

### 6. **Acesse a API**
- 🌐 **URL Base:** `http://localhost:5000`
- 📊 **Health Check:** `http://localhost:5000/health`
- 📚 **Documentação:** `http://localhost:5000`

## 🧪 Executando Testes

```bash
# Executar todos os testes
pytest

# Executar com detalhes
pytest -v

# Executar com cobertura
pytest --cov=. --cov-report=html

# Executar testes específicos
pytest tests/test_users.py -v
pytest tests/test_mappings.py -v

# Executar testes em modo watch (desenvolvimento)
pytest-watch
```

## 📚 Documentação da API

### **Endpoints Principais**

#### **Usuários** (`/api/users`)
| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|---------|
| `GET` | `/api/users/` | Lista todos os usuários | ✅ |
| `GET` | `/api/users/{id}` | Busca usuário por ID | ✅ |
| `POST` | `/api/users/` | Cria novo usuário | ✅ |
| `PUT` | `/api/users/{id}` | Atualiza usuário | ✅ |
| `DELETE` | `/api/users/{id}` | Remove usuário | ✅ |

#### **Mapeamentos** (`/api/mappings`)
| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|---------|
| `GET` | `/api/mappings/` | Lista todos os mapeamentos | ✅ |
| `GET` | `/api/mappings/{id}` | Busca mapeamento por ID | ✅ |
| `POST` | `/api/mappings/` | Cria novo mapeamento | ✅ |
| `PUT` | `/api/mappings/{id}` | Atualiza mapeamento | ✅ |
| `DELETE` | `/api/mappings/{id}` | Remove mapeamento | ✅ |
| `GET` | `/api/mappings/user/{user_id}` | Mapeamentos de um usuário | ✅ |

#### **Sistema** 
| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|---------|
| `GET` | `/` | Informações da API | ✅ |
| `GET` | `/health` | Status de saúde | ✅ |

### **Exemplos de Uso**

#### **Criar um usuário**
```bash
curl -X POST http://localhost:5000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "usuario1",
    "email": "usuario1@exemplo.com"
  }'
```

#### **Criar um mapeamento**
```bash
curl -X POST http://localhost:5000/api/mappings/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Mapeamento Exemplo",
    "description": "Descrição do mapeamento",
    "source_data": {"campo1": "valor1"},
    "target_schema": {"campo1": "string"},
    "created_by": 1
  }'
```

#### **Listar todos os usuários**
```bash
curl -X GET http://localhost:5000/api/users/
```

## 🏗️ Estrutura do Projeto

```
Mapper-Server/
├── 📁 app.py                 # Aplicação principal Flask
├── 📁 config.py             # Configurações por ambiente
├── 📁 requirements.txt      # Dependências do projeto
├── 📁 README.md            # Documentação (este arquivo)
├── 📁 run.py               # Script de execução personalizado
├── 📁 wsgi.py              # Entry point para produção
├── 📁 .env                 # Variáveis de ambiente (criar)
├── 📁 env.example          # Exemplo de variáveis de ambiente
├── 📁 pytest.ini          # Configuração do pytest
│
├── 📁 database/            # Camada de dados
│   ├── 📁 __init__.py
│   ├── 📁 database.py     # Inicialização do banco
│   └── 📁 models.py       # Modelos SQLAlchemy
│
├── 📁 routes/              # Camada de rotas
│   ├── 📁 __init__.py
│   ├── 📁 users.py        # Endpoints de usuários
│   └── 📁 mappings.py     # Endpoints de mapeamentos
│
├── 📁 utils/               # Utilitários
│   ├── 📁 __init__.py
│   └── 📁 helpers.py      # Funções auxiliares
│
├── 📁 tests/               # Testes automatizados
│   ├── 📁 __init__.py
│   ├── 📁 test_users.py   # Testes de usuários
│   └── 📁 test_mappings.py # Testes de mapeamentos
│
└── 📁 venv/                # Ambiente virtual Python
```

## ⚙️ Configuração

### **Variáveis de Ambiente**

| Variável | Descrição | Padrão | Obrigatória |
|----------|-----------|---------|-------------|
| `FLASK_ENV` | Ambiente da aplicação | `development` | ❌ |
| `SECRET_KEY` | Chave secreta Flask | `dev-secret-key-change-in-production` | ❌ |
| `DATABASE_URL` | URL do banco de dados | `sqlite:///mapper.db` | ❌ |
| `PORT` | Porta da aplicação | `5000` | ❌ |
| `HOST` | Host da aplicação | `0.0.0.0` | ❌ |
| `DEBUG` | Modo debug | `False` | ❌ |

### **Ambientes Disponíveis**

- **`development`** - Modo de desenvolvimento com debug ativado
- **`production`** - Modo de produção otimizado
- **`testing`** - Modo de teste com banco separado

## 🗄️ Banco de Dados

### **Inicialização Automática**
O banco SQLite será criado automaticamente na primeira execução da aplicação.

### **Migrações (Opcional)**
```bash
# Inicializar sistema de migrações
flask db init

# Criar nova migração
flask db migrate -m "Initial migration"

# Aplicar migrações
flask db upgrade

# Reverter migração
flask db downgrade
```

### **Modelos de Dados**
- **`User`** - Usuários do sistema
- **`Mapping`** - Mapeamentos de dados
- **Relacionamentos** - Usuários podem ter múltiplos mapeamentos

## 🚀 Deploy

### **Docker (Recomendado)**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Expor porta
EXPOSE 5000

# Comando de execução
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "wsgi:app"]
```

### **Docker Compose**
```yaml
version: '3.8'
services:
  mapper-server:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - ./data:/app/data
```

### **Heroku**
```bash
# Criar aplicação
heroku create mapper-server

# Configurar variáveis
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=sua-chave-secreta

# Deploy
git push heroku main
```

### **VPS/Server**
```bash
# Instalar dependências do sistema
sudo apt update
sudo apt install python3 python3-pip python3-venv nginx

# Configurar aplicação
cd /var/www/mapper-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configurar systemd service
sudo systemctl enable mapper-server
sudo systemctl start mapper-server

# Configurar Nginx como proxy reverso
sudo nano /etc/nginx/sites-available/mapper-server
```

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Clone** seu fork: `git clone https://github.com/seu-usuario/mapper-server.git`
3. **Crie** uma branch para sua feature: `git checkout -b feature/AmazingFeature`
4. **Commit** suas mudanças: `git commit -m 'Add some AmazingFeature'`
5. **Push** para a branch: `git push origin feature/AmazingFeature`
6. **Abra** um Pull Request

### **Diretrizes de Contribuição**
- Siga o padrão de código existente
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Use mensagens de commit descritivas

## 🧪 Testes

### **Executando Testes**
```bash
# Testes básicos
pytest

# Testes com detalhes
pytest -v

# Testes com cobertura
pytest --cov=. --cov-report=html

# Testes específicos
pytest tests/test_users.py::test_create_user -v
```

### **Cobertura de Testes**
- **Usuários:** 100% cobertura
- **Mapeamentos:** 100% cobertura
- **Utilitários:** 100% cobertura
- **Total:** 100% cobertura

## 📊 Status do Projeto

- ✅ **API REST** - Implementada e testada
- ✅ **Banco de dados** - Configurado e funcionando
- ✅ **Testes** - 11 testes passando
- ✅ **Documentação** - README completo
- ✅ **Configuração** - Múltiplos ambientes
- ✅ **Deploy** - Instruções para múltiplas plataformas

## 🆘 Suporte

### **Problemas Comuns**

#### **Erro: "No module named 'flask'"**
```bash
# Solução: Ativar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
```

#### **Erro: "Port already in use"**
```bash
# Solução: Mudar porta no arquivo .env
PORT=5001
```

#### **Erro: "Database locked"**
```bash
# Solução: Verificar se não há outra instância rodando
# Ou deletar o arquivo de banco e recriar
```

### **Canais de Suporte**
- 📧 **Issues:** [GitHub Issues](https://github.com/seu-usuario/mapper-server/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/seu-usuario/mapper-server/discussions)
- 📚 **Documentação:** Este README

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- **Flask** - Framework web elegante e flexível
- **SQLAlchemy** - ORM poderoso para Python
- **pytest** - Framework de testes robusto
- **Comunidade Python** - Suporte e contribuições

## 🔄 Changelog

### **[v1.0.0]** - 2024-01-XX
#### **Adicionado**
- ✨ Implementação inicial da API REST
- 🗄️ Sistema de banco de dados SQLite + SQLAlchemy
- 👤 Endpoints para gerenciamento de usuários
- 🗺️ Endpoints para gerenciamento de mapeamentos
- 🧪 Sistema de testes automatizados com pytest
- ⚙️ Configurações por ambiente (dev, prod, test)
- 📚 Documentação completa da API
- 🔒 Tratamento de segurança e validação de dados

#### **Técnico**
- 🏗️ Arquitetura modular com blueprints Flask
- 🔄 Factory pattern para criação de aplicação
- 📊 Tratamento centralizado de erros
- 🌐 Suporte a CORS para integração com clientes
- 📝 Logs estruturados e monitoramento

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela!**

[![GitHub stars](https://img.shields.io/github/stars/seu-usuario/mapper-server?style=social)](https://github.com/seu-usuario/mapper-server)
[![GitHub forks](https://img.shields.io/github/forks/seu-usuario/mapper-server?style=social)](https://github.com/seu-usuario/mapper-server)
[![GitHub issues](https://img.shields.io/github/issues/seu-usuario/mapper-server)](https://github.com/seu-usuario/mapper-server/issues)

</div>

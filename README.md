# BookStore API

API REST para sistema de livraria desenvolvida com Django REST Framework.

## 🚀 Deploy

- **Produção:** https://josedev.pythonanywhere.com/
- **Admin:** https://josedev.pythonanywhere.com/admin/

## 📋 Endpoints Principais

| Endpoint | Descrição |
|----------|-----------|
| `/` | Página inicial com lista de endpoints |
| `/admin/` | Painel administrativo Django |
| `/hello/` | Hello World |
| `/bookstore/v1/` | API v1 (orders e products) |
| `/bookstore/v2/` | API v2 (orders e products) |
| `/api-token-auth/` | Autenticação por token |
| `/update_server/` | Webhook para atualização automática |

## 🛠️ Tecnologias

- **Backend:** Django 4.x + Django REST Framework
- **Banco:** SQLite3 
- **Deploy:** PythonAnywhere
- **Gerenciamento:** Poetry
- **Versionamento:** Git/GitHub

## ⚡ Como Usar

### 1. **Acessar API:**
```bash
curl https://josedev.pythonanywhere.com/bookstore/v1/
```

### 2. **Autenticação por Token:**
```bash
curl -X POST https://josedev.pythonanywhere.com/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_user", "password": "sua_senha"}'
```

### 3. **Admin Panel:**
- Acesse: https://josedev.pythonanywhere.com/admin/
- Login com credenciais de superusuário

## 📦 Como Foi Construído

### 1. **Setup Inicial**
```bash
# Criar projeto Django
django-admin startproject bookstore
cd bookstore

# Configurar Poetry
poetry init
poetry add django djangorestframework
```

### 2. **Apps Criados**
- `product/` - Gerenciamento de produtos e categorias
- `order/` - Gerenciamento de pedidos
- `bookstore/` - Configurações principais

### 3. **Estrutura API**
- **Models:** Product, Category, Order
- **Serializers:** Para conversão JSON
- **ViewSets:** CRUD operations
- **URLs:** Versionamento v1/v2

### 4. **Deploy PythonAnywhere**
```bash
# 1. Upload código para GitHub
git push origin main

# 2. Clone no PythonAnywhere  
git clone https://github.com/SantosJI4/BookStore.git
cd BookStore

# 3. Instalar dependências
poetry install

# 4. Configurar WSGI
# Arquivo: /var/www/josedev_pythonanywhere_com_wsgi.py

# 5. Coletar static files
poetry run python manage.py collectstatic

# 6. Configurar virtualenv no painel Web
# Path: /home/josedev/.cache/pypoetry/virtualenvs/...

# 7. Reload aplicação
```

### 5. **Configurações Importantes**

#### `settings.py`
```python
ALLOWED_HOSTS = ['josedev.pythonanywhere.com']
STATIC_ROOT = BASE_DIR / "staticfiles"
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

#### Auto-Deploy
- Webhook configurado em `/update_server/`
- Permite atualização automática via GitHub

## 🔧 Desenvolvimento Local

```bash
# Clone o repositório
git clone https://github.com/SantosJI4/BookStore.git
cd BookStore

# Instalar dependências
poetry install

# Ativar ambiente
poetry shell

# Migrations
python manage.py migrate

# Criar superuser
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver
```

Acesse: http://localhost:8000/

## 📁 Estrutura do Projeto

```
BookStore/
├── bookstore/           # Configurações Django
├── order/              # App de pedidos
├── product/            # App de produtos  
├── static/             # Arquivos estáticos
├── pyproject.toml      # Dependências Poetry
├── manage.py           # Django CLI
└── README.md          # Este arquivo
```

## ✨ Features

- ✅ API REST completa
- ✅ Versionamento de API (v1/v2)  
- ✅ Autenticação por token
- ✅ Paginação automática
- ✅ Admin panel Django
- ✅ Deploy automatizado
- ✅ Static files configurados
- ✅ Webhook para auto-update

---

**Desenvolvido por:** José Santos  
**Deploy:** PythonAnywhere  
**Repositório:** https://github.com/SantosJI4/BookStore

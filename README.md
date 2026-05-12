# QA Automation — Petstore API & SauceDemo Web

Projeto de automação de testes com cobertura completa de API REST e testes Web E2E, integrado com pipeline CI/CD via GitHub Actions.

## Tecnologias

- Python 3.12
- Pytest
- Selenium 4
- Requests
- Faker
- pytest-html
- GitHub Actions

## Estrutura do Projeto
```bash
qa-automation-project/
├── .github/workflows/qa-pipeline.yml
├── tests/
│   ├── api/
│   │   ├── user/test_user.py
│   │   ├── store/test_store.py
│   │   └── pet/test_pet.py
│   └── web/
│       ├── pages/
│       │   ├── login_page.py
│       │   ├── inventory_page.py
│       │   ├── cart_page.py
│       │   └── checkout_page.py
│       └── flows/
│           └── test_checkout_flow.py
├── conftest.py
└── requirements.txt
```
## EndPoints Cobertos
```bash
API — Swagger Petstore (19 endpoints)
Pet (7):

POST /pet — Criar pet
GET /pet/{petId} — Buscar pet por ID
PUT /pet — Atualizar pet
POST /pet/{petId} — Atualizar pet com form data
DELETE /pet/{petId} — Deletar pet
GET /pet/findByStatus — Buscar pets por status
POST /pet/{petId}/uploadImage — Upload de imagem

Store (4):

POST /store/order — Criar pedido
GET /store/order/{orderId} — Buscar pedido por ID
DELETE /store/order/{orderId} — Deletar pedido
GET /store/inventory — Consultar inventário

User (8):

POST /user — Criar usuário
GET /user/{username} — Buscar usuário
PUT /user/{username} — Atualizar usuário
DELETE /user/{username} — Deletar usuário
GET /user/login — Login
GET /user/logout — Logout
POST /user/createWithArray — Criar usuários em array
POST /user/createWithList — Criar usuários em lista
```
## Cenarios WEB cobertos
```bash

Login com credenciais válidas
Login com credenciais inválidas
Login com usuário bloqueado
Fluxo completo E2E: login → adicionar ao carrinho → checkout → confirmação
Checkout sem preencher campos obrigatórios
```
## Como Instalar

```bash
git clone https://github.com/seu-usuario/qa-automation-project.git
cd qa-automation-project
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Como Executar

```bash
# Todos os testes
pytest tests/ -v

# Apenas API
pytest tests/api/ -v

# Apenas Web
pytest tests/web/ -v

# Com relatório HTML
pytest tests/ -v --html=reports/resultado.html --self-contained-html
```

## Estratégia de Testes

### API — Swagger Petstore
Cobertura completa dos endpoints de **Pet** (7), **Store** (4) e **User** (8). Cada teste valida status code e corpo da resposta. Dados gerados dinamicamente com Faker para evitar colisão entre execuções.

### Web — SauceDemo E2E
Fluxo ponta a ponta utilizando **Page Object Model**: login, adição ao carrinho e finalização de compra. Inclui cenários negativos como login inválido, usuário bloqueado e checkout sem preencher campos.

### CI/CD
Pipeline no GitHub Actions dispara automaticamente em todo push ou pull request, executando API e Web em paralelo e publicando relatórios HTML como artefatos.

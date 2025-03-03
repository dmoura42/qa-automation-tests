# Sistema de Automação de Testes para uma API de Gestão de Usuários

Este projeto tem como objetivo criar um sistema de automação de testes para uma API de gestão de usuários, abordando testes unitários, testes de API, automação web e integração com DevOps.

## 📌 Tecnologias Utilizadas
- **Python**
- **Pytest** para execução de testes
- **Requests** para testes de API
- **Selenium** para automação web
- **Robot Framework** para estruturação de testes
- **GitHub Actions/Azure DevOps** para integração contínua

## 📂 Estrutura do Projeto
```
qa-automation-tests/
│-- src/               # Código da API fictícia para testes
│-- tests/
│   ├── unit/         # Testes unitários
│   ├── api/          # Testes de API
│   ├── web/          # Testes de automação web
│-- requirements.txt   # Dependências do projeto
│-- README.md          # Documentação do projeto
```

## 🚀 Como Executar o Projeto
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/qa-automation-tests.git
cd qa-automation-tests
```

### 2️⃣ Criar Ambiente Virtual e Instalar Dependências
```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate  # Windows  
pip install -r requirements.txt
```

### 3️⃣ Executar Testes
Para rodar os testes unitários:
```bash
pytest tests/unit
```

Para rodar os testes de API:
```bash
pytest tests/api
```

Para rodar os testes web (Selenium):
```bash
pytest tests/web
```

## 📜 Licença
Este projeto está licenciado sob a **MIT License**.


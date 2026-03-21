# 📝 API CRUD de Tarefas com Flask

Este projeto é uma API RESTful simples para gerenciamento de tarefas (to-do list), desenvolvida com Flask. Ideal para estudos de back-end, conceitos de API REST, e prática com Python.

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Flask
* pytest
* Git
* Postman
* Swagger

---

## 📂 Estrutura do Projeto

```
project/
│
├── app.py              # Arquivo principal da aplicação com as Rotas da API
├── models/             # Definição de dados
        │
        ├── task.py
├── tests.py           # Testes Unitários utilizando a biblioteca pytests
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 📌 Endpoints da API

### 🔹 Criar uma tarefa

**POST /tasks**

```json
{
  "title": "Estudar Flask",
  "description": "Praticar criação de APIs",
  "completed": false
}
```

---

### 🔹 Listar todas as tarefas

**GET /tasks**

---

### 🔹 Buscar uma tarefa por ID

**GET /tasks/int:id**

---

### 🔹 Atualizar uma tarefa

**PUT /tasks/int:id**

```json
{
  "title": "Estudar Flask",
  "description": "Atualizado",
  "completed": false
}
```

---

### 🔹 Deletar uma tarefa

**DELETE /tasks/int:id**

---

## 🧪 Testando a API

Você pode testar os endpoints utilizando ferramentas como:

* Postman
* Insomnia
* curl (linha de comando)

Exemplo com curl:

```bash
curl -X GET http://127.0.0.1:5000/tasks
```

---

## 📚 Documentação da API

### 🔹 Swagger (arquivo)
./docs/swagger.json

### 🔹 Postman

- 📥 Download da collection: ./docs/postman_collection.json

## 🧠 Conceitos Praticados

* Arquitetura REST
* Métodos HTTP (GET, POST, PUT, DELETE)
* Estruturação de projetos Flask
* Manipulação de JSON
* Boas práticas de API

---

## 📌 Melhorias Futuras

* Integração com banco de dados (SQLite, PostgreSQL)
* Autenticação com JWT
* Documentação com Swagger
* Validação de dados
* Paginação e filtros

---

## 🤝 Contribuição

Sinta-se livre para contribuir com melhorias!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é livre para uso educacional.

---

## 👨‍💻 Autor

Desenvolvido para fins de estudo e prática com Flask.

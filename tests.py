import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova Tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    
    response_json = response.json()
    assert "Message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    response_json = response.json()
    assert response.status_code == 200
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_list_tasks():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "title": "Título de Teste",
            "description": "Descrição atualizada pytest",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "Message" in response_json
        
        #Verifica se o corpo da requisição está realmente igual ao que foi passado no payload acima
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]
        
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        
        #Faz a requisição novamente e caso o id não exista significa que a 
        # task foi realmente deletada retornando o status_code 404
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
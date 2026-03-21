from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({
        "Message": "Tarefa criada com sucesso"
    })
    
@app.route("/tasks", methods=["GET"])
def list_tasks():
    if not tasks:
        return jsonify({"Message": "Lista Vazia, adicione uma tarefa na sua lista"}), 404
    else:
        task_list = [task.to_dict() for task in tasks]
        output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({
        "Message": "Não foi possivel encontrar a atividade"
        }), 404

if __name__ == "__main__":
    app.run(debug=True)

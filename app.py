from flask import Flask, request
from models.task import Task
from flasgger import Swagger

app = Flask(__name__)
Swagger(app, template_file="swagger.yaml")

tasks = []

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request
from models.task import Task

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["GET"])
def create_task():
    data = request.get_json()
    
    return data

if __name__ == "__main__":
    app.run(debug=True)

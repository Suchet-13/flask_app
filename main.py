from asyncio import tasks
from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "Contact": "9607211912",
        "Name": "Suchet",
        "done": False,
        "id":1
    },
    {
        "Contact": "9943547892",
        "Name": "Ramesh",
        "done":False,
        "id":2
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": data
    })

if (__name__ == "__main__"):
    app.run(debug=True)
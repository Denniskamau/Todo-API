from flask_api import FlaskAPI
from flask import request

app = FlaskAPI(__name__)


#POST endpoint
todos =[]
number = 0
@app.route('/api/', methods= ['POST'])
def create_todo():
    try:
        if request.method == 'POST':
            data={"id":number, "title":request.data.title,"done":request.data.done,"todo":request.data.todos}
            todos.append(data)
            number +=1
            response = {"status":201,"message":"data saved", "data":request.data}
            return response
    except Exception as e:
        response = {"status":"403","message":e}
        return response
@app.route('/api/',methods=['GET'])
def get_all_todos():
    try:
        if request.method == 'GET':
            response = {"status":200,"data":todos}
            return response
    except Exception as e:
        response = {"status":"403","message":e}
        return response

@app.route('/api/<int:key>',methods=['GET'])
def get_one_todo(key):
    try:
        if request.method == 'GET':
            for todo in todos:
                if todo.id == key:
                    response = {"status":200,"message":"succesful", "data":todo}
                    return response
    except Exception as e:
        response = {"status":"403","message":e}
        return response

@app.route('/api/<int:key>', methods=['DELETE'])
def delete_todos(key):
    try:
        if request.method == 'DELETE':
            for todo in todos:
                if todo.id == key:
                    todos.pop(todo)
                    response = {"status":200, "message":"delete succesful"}

            return response
    except Exception as e:
        response = {"status":"403","message":e}
        return response

@app.route('/api/<int:key>', methods=['PUT'])
def update_todo(key):
    try:
        if request.method == 'PUT':
            for todo in todos:
                if todo.id == key:
                    todos.title = request.data.title
                    todos.done = request.data.done
                    todos.todo = request.data.todo
                response = {"status":200,"message":"update succesful"}
            return response
    except Exception as e:
        response = {"status":"403","message":e}
        return response

if __name__ == "__main__":
    app.run(debug=True)
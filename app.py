from flask_api import FlaskAPI
from flask import request,jsonify,abort

app = FlaskAPI(__name__)

"""
URL =http://127.0.0.1:5000/api/
For a database I am using a list with dict objects to represent each todo
"""
todos =[
       {
        'id': 1,
        'title': u'Finish Api',
        'description': u'Finish this api and submit',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
#POST endpoint
@app.route('/api/', methods= ['POST'])
def create_todo():
    try:
        if not request.json or not 'title' in request.json or not 'done' in request.json:
            return jsonify({'message':'malformed json object'}), 400
        todo = {
            'id': todos[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        todos.append(todo)
        return jsonify({'todo':todo}), 201
    except Exception as e:
        response = {"status":"403","message":e}
        return response

# GET all  todos endpoint
@app.route('/api/',methods=['GET'])
def get_all_todos():
    try:
        if request.method == 'GET':
            response = {"status":200,"data":todos}
            return jsonify({"todos":response})
    except Exception as e:
        response = {"status":"403","message":e}
        return response

#Get one todo
@app.route('/api/<int:todo_id>',methods=['GET'])
def get_one_todo(todo_id):
    try:
        if request.method == 'GET':
            todo = [todo for todo in todos if todo['id'] == todo_id]
            if len(todo) == 0:
                return jsonify({'message':'No record with that id'}), 400
            return jsonify({'todo': todo[0]})
    except Exception as e:
        response = {"status":"403","message":e}
        return response


#Delete a todo
@app.route('/api/<int:todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    try:
        if request.method == 'DELETE':
            todo = [todo for todo in todos if todo['id'] == todo_id]
            if len(todo) == 0:
                return jsonify({'message':'No record with that id'}), 400
            todos.remove(todo[0])
            return jsonify({'message':"succesful"}),204
    except Exception as e:
        response = {"status":"403","message":e}
        return response


#Update a todo
@app.route('/api/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    try:
        if request.method == 'PUT':
            todo = [todo for todo in todos if todo['id'] == todo_id]
            todo[0]['title'] = request.json.get('title', todo[0]['title'])
            todo[0]['description'] = request.json.get('description', todo[0]['description'])
            todo[0]['done'] = request.json.get('done', todo[0]['done'])
            return jsonify({'todo': todo[0]}),200
    except Exception as e:
        response = {"status":"403","message":e}
        return response

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)
task = [
    {
        'id': 1, 
        'title': 'Buy Groceries',
        'description': 'Milk, Cheese, Pizza',
        'done': False
    },
    {
        'id': 2, 
        'title': 'Learn Python',
        'description': 'Find a good Python Tutorial on Web.',
        'done': False
    }
]
@app.route('/add-data', methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Please Provide the Data',
        },400)
        task = {
            'id': tasks[-1]['id'] + 1, 
            'title': request.json['title'],
            'description': request.json.get('description', ''),
            'done': False
        }
        tasks.append(task)
        return jsonify({
            "status": "sucess",
            "message": "Task Added Sucessfully"
        })
@app.route('/get-data', methods = ['GET'])
def get_task():
    return jsonify({
        "data": tasks
    })

if __name__ == '__main__':
    app.run(debug = True)













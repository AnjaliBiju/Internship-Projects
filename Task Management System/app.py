from flask import Flask, request, jsonify
from service import TaskManager

app=Flask(__name__)
tm= TaskManager()

@app.route('/')
def home():
    return "Task Management API is currently running"

#Create User
@app.route('/users', methods=['POST'])
def create_user():
    data= request.json
    user_id= data.get('user_id')
    name= data.get('name')
    email= data.get('email')
    tm.create_user(user_id,name,email)
    return jsonify({'message':f'User {user_id} created'}),201

#Create Task
@app.route('/tasks',methods=['POST'])
def create_task():
    data=request.json
    task_id= data.get('task_id')
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority')
    due_date = data.get('due_date')
    status = data.get('status')
    assigned_to = data.get('assigned_to', None)
    tm.create_task(task_id, title, description, priority, due_date, status, assigned_to)
    return jsonify({'message':f'Task {task_id} created'}), 201

#Assign task to user
@app.route('/tasks/<int:task_id>/assign/<int:user_id>', methods=['PUT'])
def assign_task(task_id, user_id):
    tm.assign_task_to_user(task_id, user_id)
    return jsonify({'message':f'Task {task_id} assigned to User {user_id}'}), 200

#Get all tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    try:
        conn= tm.conn or tm._get_connection()
        cursor= conn.cursor()
        cursor.execute("""SELECT t.task_id, t.title, t.status, t.priority, t.due_date, u.name 
                       FROM Task t LEFT JOIN User u ON t.assigned_to= u.user_id
                       """)
        tasks= cursor.fetchall()
        result=[]
        for t in tasks:
            result.append({
                'task_id': t[0],
                'title': t[1],
                'status': t[2],
                'priority': t[3],
                'due_date': str(t[4]),
                'assigned_to': t[5] or "Unassigned"
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error':str(e)}),500
    
#Get tasks by user
@app.route('/users/<int:user_id>/tasks',methods=['GET'])
def get_tasks_by_user(user_id):
    try:
        conn= tm.conn or tm._get_connection()
        cursor= conn.cursor()
        cursor.execute("""SELECT task_id, title, status, priority, due_date
                       FROM Task WHERE assigned_to = %s
                       """,(user_id,))
        tasks= cursor.fetchall()
        result=[]
        for t in tasks:
            result.append({
                'task_id': t[0],
                'title': t[1],
                'status': t[2],
                'priority': t[3],
                'due_date': str(t[4])
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
#Delete task
@app.route('/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    tm.delete_task(task_id)
    return jsonify({'message':f'Task {task_id} deleted'}), 200

#Close db
@app.route('/shutdown', methods=['POST'])
def shutdown():
    tm.close()
    return jsonify({'message': 'Database connection closed'}), 200

if __name__=='__main__':
    app.run(debug=True)

from typing import List
from models import Task
from models import User
from config import get_connection

class TaskManager:
    """Handles creation, management and organization of tasks and users"""
    
    def __init__(self):
        self.tasks: List[Task]= []
        self.users: List[User]= []
        self.conn= get_connection()
        self.cursor= self.conn.cursor()
        
    def _get_connection(self):
        return get_connection()
        
    def create_task(self,task_id, title, description, priority, due_date, status, assigned_to):
        """Creates a new task and adds it to the task list"""
        try:
            conn= get_connection()
            cursor= conn.cursor()
            cursor.execute("""INSERT INTO Task(task_id, title, description, priority, due_date, status, assigned_to)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                            ,(task_id, title, description, priority, due_date, status, assigned_to))
            conn.commit()
            conn.close()
            print(f"Task {task_id} created successfully")
        except Exception as e:
            print(f"Error creating a new task: {e}")
            
    def delete_task(self,task_id):
        """Deletes a task from the task list"""
        try:
            conn= get_connection()
            cursor= conn.cursor()
            
            cursor.execute("DELETE FROM Task WHERE task_id= %s",(task_id,))
            conn.commit()
            
            if cursor.rowcount== 0:  #if no rows were affected
                print(f"Task {task_id} not found")
            else:
                print(f"Task {task_id} deleted successfully")
            conn.close()
        except Exception as e:
            print(f"Error deleting task: {e}")
                    
    def get_task(self, task_id):
        """Prints a task matching the specified task ID"""
        try:
            conn= get_connection()
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM Task WHERE task_id=%s",(task_id,))
            task= cursor.fetchone()
            conn.close()
            
            if task:
                print(task)
            else:
                print(f"Task {task_id} not found")
                            
        except Exception as e:
            print(f"Error retrieving task: {e}")
            
            
    def list_all_tasks(self):
        """Prints all tasks currently managed by the system"""
        try:
            conn= get_connection()
            cursor= conn.cursor()
            cursor.execute("SELECT * FROM Task")
            tasks= cursor.fetchall()
            conn.close()
            
            if tasks!=[]:
                for task in tasks:
                    task_id, title, description, priority, due_date, status, assigned_to= task  #unpacking
                    print(f"\n Task ID: {task_id}")
                    print(f"Title: {title}")
                    print(f"Description: {description}")
                    print(f"Priority: {priority}")
                    print(f"Due Date: {due_date}")
                    print(f"Status: {status}")
                    if assigned_to is not None:
                        print(f"Assigned To: {assigned_to}")
                    else:
                        print(f"Assigned To: Not assigned")
            else:
                print("No tasks available")
                
        except Exception as e:
            print(f"Error listing tasks: {e}")
                   
    def list_tasks_by_user(self, user_id):
        """Prints all tasks assigned to the specified User ID"""
        try:
            conn= get_connection()
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM User WHERE user_id=%s",(user_id,))
            user= cursor.fetchone()
            if user is None:
                print(f"No user found with User ID {user_id}")
                conn.close()
                return
            
            cursor.execute("SELECT * FROM Task WHERE assigned_to=%s",(user_id,))
            tasks= cursor.fetchall()
            conn.close()
            
            if tasks:
                print(f"Tasks assigned to User {user_id}: ")
                for task in tasks:
                    task_id, title, description, priority, due_date, status, assigned_to= task  #unpacking
                    print(f"\n Task ID: {task_id}")
                    print(f"Title: {title}")
                    print(f"Description: {description}")
                    print(f"Priority: {priority}")
                    print(f"Due Date: {due_date}")
                    print(f"Status: {status}")
                    print(f"Assigned To: {assigned_to}")
            else:
                print(f"No tasks is assigned to User {user_id}")
            
        except Exception as e:
            print(f"Error listing tasks by user: {e}")
        
    def list_tasks_by_status(self, status):
        """Prints all tasks matching the specified status"""
        try:
            validate_statuses= ['To-Do','In Progress','Done']
            if status not in validate_statuses:
                print("Invalid status. Please try again")
                return
            
            conn= get_connection()
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM Task WHERE status=%s",(status,))
            tasks= cursor.fetchall()
            conn.close()
            
            if tasks:
                print(f"Tasks with status {status}: ")
                for task in tasks:
                    task_id, title, description, priority, due_date, status, assigned_to= task  #unpacking
                    print(f"\n Task ID: {task_id}")
                    print(f"Title: {title}")
                    print(f"Description: {description}")
                    print(f"Priority: {priority}")
                    print(f"Due Date: {due_date}")
                    print(f"Status: {status}")
                    if assigned_to is not None:
                        print(f"Assigned To: {assigned_to}")
                    else:
                        print(f"Assigned To: Not assigned")
            else:
                print(f"No tasks found with status {status}")
                    
        except Exception as e:
            print(f"Error listing tasks by status: {e}")
                
    def create_user(self, user_id, name, email):
        """Creates a new user in the system"""
        try:
            conn= get_connection()
            cursor= conn.cursor()
            cursor.execute("INSERT INTO USER (user_id, name, email) VALUES (%s, %s, %s)",
                           (user_id, name, email))
            conn.commit()
            conn.close()
            print(f"User {user_id} created successfully")
        except Exception as e:
            print(f"Error creating a new user: {e}")
        
    def assign_task_to_user(self, task_id, user_id):
        """Assigns a task to the specified user"""
        try:
            conn= get_connection()
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM Task WHERE task_id=%s",(task_id,))
            task= cursor.fetchone()  #used after executing a SELECT query in Python
            if not task:
                print(f"Task {task_id} not found")
                return
            
            #Check if user exists
            cursor.execute("SELECT * FROM User WHERE user_id=%s",(user_id,))
            user= cursor.fetchone()
            if not user:
                print(f"User {user_id} not found")
                return
            
            #Assign task to user
            cursor.execute("UPDATE Task SET assigned_to=%s WHERE task_id=%s",(user_id, task_id))
            conn.commit()
            conn.close()
            print(f"Task {task_id} assigned to User {user_id}")
        except Exception as e:
            print(f"Error assigning tasks to user: {e}")        
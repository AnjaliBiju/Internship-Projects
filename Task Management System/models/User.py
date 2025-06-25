from typing import List
from .Task import Task

class User:
    """Represents a user in the task management system"""
    
    def __init__(self, user_id: int, name: str, email: str):
        """Initialise a new user with basic attributes and validation """
        
        if (isinstance(user_id,int)==False):
            raise ValueError("User ID must be an integer")
        if (name.strip()==""):
            raise ValueError("Name cannot be empty")
        if (email.strip()==""):
            raise ValueError("Email ID cannot be empty")

        self.user_id= user_id
        self.name= name
        self.email= email
        self.task_list: List[Task]= []

    def add_task(self,task):
        """Adds a task to the user's task list"""
        try:
            self.task_list.append(task)
        except Exception as e:
            print(f"An error occurred while adding task: {e}")

    def remove_task(self,task_id):
        """Removes a task from user's task list"""
        try:
            for task in self.task_list:
                if (task_id== task.task_id):
                    self.task_list.remove(task)
                    print(f"Task {task_id} removed")
                    return
            print(f"Task {task_id} not found")
        except Exception as e:
            print(f"An error occurred while removing task: {e}")

    def view_tasks_by_status(self, status):
        """Print tasks that match the specified status"""
        flag=0
        for task in self.task_list:
            if (status== task.status):
                flag=1
                print(task)
        if (flag==0):
            print("No tasks matching")

    def __str__(self):
        return f"{self.user_id}, {self.name}, {self.email}"
class Task:
    """Represents a task in the Task Management System """
    
    def __init__(self, task_id:int, title:str, description:str, priority:str, due_date:str, status:str="To Do", assigned_to=None):
        """Initialise a new task with basic attributes and validation """
        
        if (priority not in ['Low','Medium','High']):
            raise ValueError("Priority must be 'Low', 'Medium' or 'High' ")
        if (status not in ['To-Do','In Progress','Done']):
            raise ValueError("Status must be 'To-Do', 'In Progress' or 'Done'")

        self.task_id= task_id
        self.title= title
        self.description= description
        self.assigned_to= assigned_to
        self.priority= priority
        self.due_date= due_date
        self.status= status

    def update_status(self, new_status):
        """Update the task status. Raises ValueError in case of invalid status"""
        try:
            if (new_status not in ['To-Do','In Progress','Done']):
                raise ValueError("Status must be 'To-Do', 'In Progress' or 'Done'")
            self.status= new_status
        except Exception as e:
            print(f"An error occurred while updating status: {e}")

    def update_priority(self, new_priority):
        """Update the task priority. Raises ValueError in case of invalid priority"""
        try:
            if (new_priority not in ['Low','Medium','High']):
                raise ValueError("Priority must be 'Low', 'Medium' or 'High' ")
            self.priority= new_priority
        except Exception as e:
            print(f"An error occurred while updating priority: {e}")

    def assign_to(self, user):
        """Assigns the task to a user"""
        self.assigned_to= user

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.assigned_to}, {self.priority}, {self.due_date}, {self.status}"
    
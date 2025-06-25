from service import TaskManager

def main():
    tm= TaskManager()

    def get_valid_task_id():
        """Task ID must be a non-empty numeric"""
        while True:
            task_id = input("Enter Task ID: ")
            if (task_id.strip()==""):
                print("Task ID cannot be empty. Please try again.")
            elif (task_id.isdigit()==False):
                print("Task ID must be a number")
            else:
                return int(task_id)

    while True:
        print("\n\nTask Management System")
        print("1. Create User")
        print("2. Create Task")
        print("3. Assign Task to User")
        print("4. List all Tasks")
        print("5. List Tasks by User")
        print("6. List Tasks by status")
        print("7. Delete task")
        print("8. Exit")

        try:
            choice= int(input("\nEnter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a value between 1 and 8: ")
            continue

        if (choice==1):
            """
            Create User
            """
            try:
                user_id= int(input("\nEnter User ID: "))
            except ValueError:
                print("Invalid input. User ID must be a number: ")
                continue
            name= input("Enter User name: ")
            email= input("Enter User email: ")
            tm.create_user(user_id, name, email)
            print(f"User {user_id} created successfully")

        elif (choice==2):
            """
            Create Task
            """
            task_id= get_valid_task_id()
            title= input("Enter Title: ")
            description= input("Enter description: ")
            priority= input("Enter priority (Low/Medium/High): ")
            due_date= input("Enter due-date (YYYY-MM-DD): ")
            status= input("Enter status (To-Do/ In Progress/ Done): ")
            assigned_to= None
            tm.create_task(task_id, title, description, priority, due_date, status, assigned_to)

        elif (choice==3):
            """
            Assign task to user
            """
            task_id= get_valid_task_id()
            try:
                user_id= int(input("Enter User ID: "))
            except ValueError:
                print("Invalid input. User ID must be a number: ")
                continue
            tm.assign_task_to_user(task_id,user_id)

        elif (choice==4):
            """
            List all tasks
            """
            tm.list_all_tasks()

        elif (choice==5):
            """
            List tasks by User
            """
            try:
                user_id= int(input("\nEnter User ID: "))
            except ValueError:
                print("Invalid input. User ID must be a number: ")
                continue
            tm.list_tasks_by_user(user_id)

        elif (choice==6):
            """
            List tasks by status
            """
            status= input("\nEnter status: ")
            tm.list_tasks_by_status(status)

        elif (choice==7):
            """
            Delete Task
            """
            task_id= get_valid_task_id()
            tm.delete_task(task_id)

        elif (choice==8):
            """
            Exit Task Management System
            """
            print("\nExiting Task Management System.")
            break

        else:
            print("\nInvalid input")
    
if __name__=="__main__":
    main()
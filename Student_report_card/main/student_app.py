from service.student_service import StudentService
from util.exceptions import (InvalidInputError, ValidationError, StudentReportCardException, 
                             StudentNotFoundException, DuplicateRollNumberException)
from util.validators import (validate_name, validate_roll_number, validate_marks)

def get_integer_input(prompt:str)->int:
    """
    Helper function to get integer input from the user.
    - Catches ValueError if input is not an integer.
    - Raises InvalidInputError, chaining the original ValueError.
    """
    while True:
        try:
            value_str= input(prompt).strip()
            value_int= int(value_str)
            return value_int
        except ValueError as e:
            raise InvalidInputError("Invalid input. Please enter an integer.", original_exception=e) from e
            #exception chaining
            
def get_marks_input() ->list:
    """
    Helper function to get 5 subject marks from the user.
    - Uses get_integer_input for each mark.- Performs basic range validation (0-100) and raises ValidationError if out of range.
    - Performs basic range validation (0-100) and raises ValidationError if out of range.
    """
    marks=[]
    print("Enter marks for 5 subjects (0-100): ")
    for i in range(1,6):
        while True:
            try:
                mark= get_integer_input(f"Subject {i}: ")
                if (mark<0 or mark>100):
                    raise ValidationError(msg="Mark must be between 0 and 100", field=f"Subject {i}", value=mark)
                marks.append(mark)
                break   #to exit the inner loop
            except (InvalidInputError, ValidationError)as e:
                print(f"An error occurred: {e.args[0]}")
                if isinstance(e, InvalidInputError) and e.original_exception:
                    print(f"Details: {e.original_exception}")
    return marks

def print_report_card(report_data: dict):
    """
    Displays formatted report card based on dictionary data
    """
    print("\n---Report Card---")
    print(f"Name : {report_data['Name']}")
    print(f"Roll number : {report_data['Roll number']}")
    print(f"Marks : {report_data['Marks']}")
    print(f"Total marks: {report_data['Total marks']}")
    print(f"Average marks: {report_data['Average marks']}")
    print(f"Grade: {report_data['Grade']}")
    print("-------------------")

def main():
    """
    Main function to run the Student Report Card application.
    - Initializes StudentService.
    - Presents a menu to the user.
    - Handles user input for adding students, generating reports.
    - Implements robust error handling using try-except blocks for custom exceptions.
    """
    service= StudentService()
    while True:
        print("\n--- Student Report Card System Menu ---")
        print("1. Add a new student")
        print("2. Generate report card for a specific student")
        print("3. Generate report cards for all students")
        print("4. Exit")
        
        choice=input("Enter your choice: ").strip()
        
        if (choice=='1'):
            """Add a new student"""
            try:
                name= input("Enter your name: ").strip()
                validate_name(name)
                                
                roll_number= get_integer_input("Enter your Roll number: ")
                validate_roll_number(roll_number)
                                
                marks= get_marks_input()
                validate_marks(marks)
                
                student= service.add_student(name, roll_number, marks)
                print(f"Student {student.name} added successfully.")
            
            except (InvalidInputError, ValidationError, DuplicateRollNumberException) as e:
                print(f"Error: {e.args[0]}")
                if (isinstance(e,InvalidInputError) and e.original_exception):
                    print(f"Details: {e.original_exception}")
                    
            except StudentReportCardException as e:
                print(f"An application error has occurred: {e.args[0]}")
                
            except Exception as e:
                print(f"An unexpected system error has occurred: {e}")
        
        elif (choice=='2'):
            """Generate report card for a specific student"""
            try:
                roll_number= get_integer_input("Enter your Roll number: ")
                validate_roll_number(roll_number)
                
                report_data= service.generate_report_card_data(roll_number)
                print_report_card(report_data)
                
            except InvalidInputError as e:
                print(f"Error: {e.args[0]}")
                if e.original_exception:
                    print(f"Details: {e.original_exception}")
            
            except StudentNotFoundException as e:
                print(f"Error: {e.args[0]} (Roll number: {e.roll_number})")
                
            except StudentReportCardException as e:
                print(f"An application error occurred: {e.args[0]}")
                
            except Exception as e:
                print(f"An unexpected system error occurred: {e}")
                
        elif (choice=='3'):
            """Generate report cards for all students"""
            try:     
                all_students= service.get_all_students()
                if (all_students==[]):
                    print("No students exist")
                    return
                else:
                    for student in all_students:
                        roll_number= student.roll_number
                        report_data= service.generate_report_card_data(roll_number)
                        print_report_card(report_data)
                        
            except StudentReportCardException as e:
                print(f"An application error occurred: {e.args[0]}")
            except Exception as e:
                print(f"An unexpected system error has occurred: {e.args[0]}")
                
        elif (choice=='4'):
            print("Exiting StudentReport Card System")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4")

if __name__=="__main__":
    main()
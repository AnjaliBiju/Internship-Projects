from dto import Student
from util.exceptions import (StudentNotFoundException,
DuplicateRollNumberException, ValidationError)
from util.validators import (validate_name, validate_roll_number, validate_marks)

class StudentService:
    def __init__(self):
       """
       Initializes the student service with an in-memory dictionary
       to store Student objects, keyed by roll number.
       """
       self._students= {} 
       
    def add_student(self, name:str, roll_number:int, marks:list) -> Student:
        """
        Adds a new student after validation.

        Args:
            name (str): The name of the student.
            roll_number (int): The unique roll number of the student.
            marks (list[int]): The marks scored in 5 subjects.

        Returns:
            Student: The newly created student object.

        Raises:
            ValidationError: If any of the input validations fail.
            DuplicateRollNumberException: If a student with the roll number already exists.
        """
        try:
            validate_name(name)
            validate_roll_number(roll_number)
            validate_marks(marks)
        except ValidationError as e:
            raise ValidationError(f"Validation error occurred: {e.msg}",field=e.field, value=e.value)
                        
        if (roll_number in self._students):
            raise DuplicateRollNumberException(
                msg="Duplicate roll number detected",
                roll_number= roll_number
            )
        #create Student object
        student= Student(name, roll_number, marks)
        #store in internal dictionary
        self._students[roll_number]= student
        return student
    
    def get_student(self, roll_number: int)->Student:
        """
        Returns:
            Student: The student object corresponding to the roll number.

        Raises:
            StudentNotFoundException: If student is not found.
        """
        if (roll_number in self._students):
            return self._students[roll_number]
        else:
            raise StudentNotFoundException(msg="Student not found", roll_number= roll_number)
    
    def get_all_students(self)->list[Student]:
        return list(self._students.values())
    
    def calculate_total(self, student:Student)->int:
        total= sum(student.marks)
        return total
    
    def calculate_average(self, student:Student)->float:
        total = self.calculate_total(student)
        avg= total/5
        return avg
    
    def get_grade(self, student:Student)->str:
        """
        Determines the grade based on the student's average marks.
        - Average >= 90 -> A
        - Average >= 75 -> B
        - Average >= 60 -> C
        - Average >= 50 -> D
        - Otherwise -> F
        """
        avg= self.calculate_average(student)
        if (avg>=90):
            return "A"
        elif (avg>=75):
            return "B"
        elif (avg>=60):
            return "C"
        elif (avg>=50):
            return "D"
        else:
            return "F"
        
    def generate_report_card_data(self, roll_number:int)->dict:
        """
        Generates all necessary data for a student's report card.
        """   
        student= self.get_student(roll_number)
        total= self.calculate_total(student)
        avg= self.calculate_average(student)
        grade= self.get_grade(student)
        
        student_dict= {"Name":student.name, "Roll number": student.roll_number, "Marks":student.marks,
                       "Total marks":total, "Average marks":avg, "Grade":grade}
        return student_dict

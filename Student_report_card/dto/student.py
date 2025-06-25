class Student:
    """
    Represents a student entity.

    Args:
        name (str): The name of the student.
        roll_number (int): The unique roll number of the student.
        marks (list[int]): List containing marks of 5 subjects.

    Returns:
        Student: The created student object.

    Raises:
        None
    """
    
    def __init__(self, name:str, roll_number:int, marks:list):
        self.name=name
        self.roll_number= roll_number
        self.marks= marks
        
    def __str__(self):
        return f"Student( Name: {self.name}\n Roll number: {self.roll_number}\n Marks: {self.marks})"
    
    def __repr__(self):
        """Return a developer friendly representation of Student object"""
        return (f"Student(Name: '{self.name}', Roll number: {self.roll_number}, Marks: {self.marks})")
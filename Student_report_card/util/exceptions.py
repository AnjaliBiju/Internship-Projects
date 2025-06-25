class StudentReportCardException(Exception):
    """Base exception for the Student report card system"""
    
    def __init__(self, msg="An error occurred in the Student report card system"):
        super().__init__(msg)
        
class InvalidInputError(StudentReportCardException):
    """Raised when user input is invalid ,i.e, a non-numeric where a number is expected"""
    def __init__(self, msg="Invalid input provided", original_exception=None):
        super().__init__(msg)
        self.original_exception= original_exception
        
class ValidationError(StudentReportCardException):
    """
    Raised when data fails specific validation rules (e.g., marks out of range,
    empty strings for required fields).
    """
    def __init__(self, msg="Input validation failed.", field=None, value=None):
        super().__init__(msg)
        self.field= field
        self.value= value
        
class StudentNotFoundException(StudentReportCardException):
    """
    Raised when a requested student (eg: by roll number) is not found in the system.
    """
    def __init__(self, msg="Student not found.", roll_number=None):
        super().__init__(msg)
        self.roll_number= roll_number
        
class DuplicateRollNumberException(StudentReportCardException):
    """
    Raised when attempting to add a student with a roll number that already exists.
    """
    def __init__(self, msg="Student with this roll number already exists", roll_number=None):
        super().__init__(msg)
        self.roll_number= roll_number
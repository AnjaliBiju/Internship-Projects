from util.exceptions import ValidationError

def validate_name(name):
    """
    Validates a student's name.
    - Should not be empty or consist only of whitespace.
    - Should be a string.
    Raises ValidationError if invalid.
    """
    
    if (isinstance(name,str)==False):
        raise ValidationError(
            msg= "Name must be a string",
            field= "name",
            value= name
        )
    if (name.strip()==""):
        raise ValidationError(
            msg= "Name cannot be empty or whitespaces",
            field= "name",
            value=name
        )
        
def validate_roll_number(roll_number):
    """
    Validates a student's roll number.
    - Must be an integer.
    - Must be a positive integer.
    Raises ValidationError if invalid.
    """
    if (isinstance(roll_number,int)==False):
        raise ValidationError(msg="Roll number must be an integer", field="roll_number", value=roll_number)
    if (roll_number<=0):
        raise ValidationError(msg="Roll number must be a positive integer", field="roll_number", value=roll_number)

def validate_marks(marks): 
    """
    Validates student's marks.
    - Must be a list.
    - All items must be integers.
    - Each mark should be in the range 0 to 100.
    """
    if (isinstance(marks,list)==False):
        raise ValidationError(msg="Marks must be a list", field="marks", value=mark)
    
    for mark in marks:
        if (isinstance(mark,int)==False):
            raise ValidationError(msg="Each mark must be an integer", field="marks", value=mark)
        if(mark<0 or mark>100):
            raise ValidationError(msg="Marks must be between 0 and 100", field="marks", value= mark)

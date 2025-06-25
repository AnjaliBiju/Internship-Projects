"""
Utility package for validations and custom exceptions used in the student report card system
"""
from .exceptions import (
    StudentReportCardException,
    InvalidInputError,
    ValidationError,
    StudentNotFoundException,
    DuplicateRollNumberException
)

from .validators import (
    validate_name,
    validate_roll_number,
    validate_marks
)
# This file contains the SensorException class, which is used to handle exceptions in the sensor module.
# It provides a detailed error message including the file name and line number where the exception occurred.
# The class inherits from the built-in Exception class and overrides the __init__ and __str__ methods to customize the error message.
# The get_detailed_error_message method is used to construct the detailed error message.
# The traceback module is used to extract the file name and line number from the exception traceback.
# The sys module is used to access the exception information.
import traceback
import sys

class SensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(str(error_message))
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    def get_detailed_error_message(self, error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in script: [{file_name}] at line [{line_number}] with message: {error_message}"

    def __str__(self):
        return self.error_message
    
    
    
    
    
    
    
    
    
    
# import sys
# import os

# def error_message_detail(error, error_detail: sys):
#     _, _, exc_tb = error_detail.exc_info()
#     filename = exc_tb.tb_frame.f_code.co_filename
    
#     error_message = "error occurred and the file name is [{o}] and the line number is [{1}] and error is [{2}]".format(
#         filename,exc_tb.tb_lineno,str(error))
    
#     return error_message
# class SensorException(Exception):
#     def __init__(self, error_message, error_detail: sys):
#         super().__init__(error_message)
#         self.error_message = error_message = error_message_detail(error_message, error_detail = error_detail)
#     def __str__(self):
#         return self.error_message
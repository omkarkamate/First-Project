from Src.Stress_Level.Logging import logging
import sys
from Src.Stress_Level.Logging import logging

def err_details(msg,err_detail:sys):
    _,_,exc_tb=err_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_message=str(err_detail.exc_info())
    return f"Error occurred in script: {file_name} at line number: {line_number} with error message: {error_message}"

class Cu_Exception(Exception):
    def __init__(self,msg,err_detail:sys):
        super().__init__(msg)
        self.msg=err_details(msg,err_detail)
    def __str__(self):
        logging.info(self.msg)
        return self.msg
    

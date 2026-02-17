import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename #The filename where the error occurred


    error_message = "Error occured in python script [{0}] line number [{1}] error message[{2}]".format(
        file_name, #python script [{0}]
        exc_tb.tb_lineno, #The exact line number where the error happened. [{1}] 
        str(error) #error message[{2}]
    )
    #This gives very detailed debugging info.
    return error_message


#This is extending Python's built-in:
class CustomException(Exception): #So, it behaves like a normal exception but with better logging.
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #This initializes the parent Exception class.
        self.error_message = error_message_detail(error_message, error_detail=error_detail) #You override the message with detailed information.

    def __str__(self):
        return self.error_message
        '''
        So when you do:
        `print(e)`
        It prints your detailed custom message.
        '''

# if __name__=="__main__":

#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)
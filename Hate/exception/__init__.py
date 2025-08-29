import sys      # provides sys.exc_info() to extract details of the current exception

def error_message_detail(error, error_detail:sys):
    # sys.exc_info() returns a tuple:
    # (exc_type, exc_value, exc_traceback)
    # We only care about exc_tb (traceback object), so ignore others with underscores
  _, _, exc_tb = error_detail.exc_info()


# Extract the file name from the traceback’s frame → code object → filename
# exc_tb.tb_frame → current stack frame at error.
# .f_code → compiled code metadata.
# .co_filename → file where error occurred.
  file_name = exc_tb.tb_frame.f_code.co_filename


# Format a custom error message with file name, line number, and the actual error message
  error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )
  
  return error_message


class CustomException(Exception):    # Inherit from built-in Exception class
  def __init__(self, error_message, error_detail):
    """
        :param error_message: The exception message (string)
        :param error_detail: Pass sys module (to extract exc_info)
    """
    # Call parent Exception class constructor
    super().__init__(error_message)

    
    # Store the detailed error message using our helper function
    self.error_message = error_message_detail(error_message, error_detail=error_detail)


  # Override __str__ so that when this exception is printed,
    # it returns our detailed error message instead of default one
  def __str__(self):
    return self.error_message
# main.py
import logging
from calculations import calculate_mean, EmptyListError

# Configure production-grade logging (writes to a file with timestamps)
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='plan_03_dsa/book_DSA_in_python/chap_01_python_primer/practicing_exception_handling/app_errors.log'  # Writes to disk instead of printing
)

def process_user_data(data):
    try:
        mean = calculate_mean(data)
        print(f"Success! The mean is {mean}")  # Prints to user
        return mean
        
    except EmptyListError as e:
        # Expected user-error. Log it as a WARNING (not ERROR), 
        # and return a user-friendly message without crashing.
        logging.warning(f"User provided empty list: {e}")
        return "No data provided to calculate average."
        
    except TypeError as e:
        # Expected programmer/user error (wrong type)
        logging.error(f"Type mismatch: {e}")
        return "Invalid data format submitted."
        
    except Exception as e:
        # CATCH-ALL for UNEXPECTED bugs (e.g., network issues, memory errors).
        # This is the ONLY place you use a broad 'except Exception'.
        logging.critical(f"UNEXPECTED CRASH in calculation: {e}", exc_info=True)
        # Send an alert to your pager (PagerDuty/Slack) here.
        return "An internal system error occurred. Our team has been alerted."

# Production entry point
if __name__ == "__main__":
    # Simulating a production request
    user_input = [1,2,'3']  
    result = process_user_data(user_input)
    print(f"Response to user: {result}")
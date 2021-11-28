import logging
import time
from datetime import datetime
import random
import sys

def generate_log(interval:float=1.0):
    """Periodically creates log messages.
    
    Every X seconds a new message is generated. The log-level is chosen randomly for each message and is either INFO,
    WARNING, ERROR or Critical with INFO being the most common level and critical a rare occurence.
    
    Parameters
    ----------
    interval : float, optional
        Time between two log messages, default is 1 second.
    """
    logging.basicConfig(level=logging.INFO)
    while True:
        time.sleep(interval)
        error_num : int = random.randint(0,99)
        timestamp : str = str(datetime.now())
        log_message : str = " generische Log-Nachricht"
            
        if error_num <= 75:
            logging.info(timestamp + " Alles ist gut.")
        elif error_num <= 90:
            logging.warning(timestamp + " Irgendetwas stimmt hier nicht...")
        elif error_num <= 97:
            logging.error(timestamp + " Ein Fehler ist aufgetreten!")
        elif error_num <= 99:
            logging.critical(timestamp + " Eine Katastrophe ist eingetreten")


if __name__ == '__main__':
    interval: float = 1.0
    if len(sys.argv) >= 2:
        interval = float(sys.argv[1])
    generate_log(interval)

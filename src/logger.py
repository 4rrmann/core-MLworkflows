#dynamic logging configuration setup
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
'''
This creates a log file like:
`02_17_2026_14_32_10.log`

Meaning:

Month
Day
Year
Hour
Minute
Second

So every run gets a unique log file.
'''

# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
'''
Creates `logs/` folder if not exists
`exist_ok=True` prevents error if folder already exists
'''

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
'''
Creates full path like:
`C:/project/logs/02_17_2026_14_32_10.log`
'''

#This configures logging globally:
logging.basicConfig(
    filename=LOG_FILE_PATH, #Logs will be saved into that file.

    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #[2026-02-17 14:35:01,123] 45 root - INFO - Model training started

    level=logging.INFO,
    #Means: INFO, WARNING, ERROR, CRITICAL
    #will be logged.

    #But DEBUG will NOT be logged.

)

'''
logging.getLogger().addHandler(logging.StreamHandler())
This will:
- Log to file
- Also show logs in terminal

Best practice for production.
'''

# if __name__=="__main__":
#     logging.info("Logging has started")
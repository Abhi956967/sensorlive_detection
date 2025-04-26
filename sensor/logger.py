# This module sets up a logger to log messages to a file in the Logs directory.
# The log file is named with the current date and time to ensure uniqueness. The logging level is set to INFO, and the log format includes the timestamp and log level.
# The logger is created using the logging.getLogger() method, which allows for logging messages throughout the application.

import logging
import os
from datetime import datetime

# Create Logs directory path
LOG_DIR = "Logs"
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), LOG_DIR, LOG_FILE)

# Make sure Logs folder exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)








# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logs_path = os.path.join(os.getcwdb(),LOG_FILE)
# os.makedirs(logs_path, exist_ok = True)
# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename = LOG_FILE_PATH,
#     format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level = logging.INFO(),
    
# )

import os
import sys
import logging

# Directory for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

# Clear old handlers to avoid duplicate logs in interactive sessions
logging.getLogger().handlers.clear()

# Configure logging
logging.basicConfig(
    level=logging.INFO, # will support - INFO, WARNING, ERROR, CRITICAL not DEBUG.
    format="[%(asctime)s: %(levelname)s: %(filename)s:%(lineno)d: %(message)s]",
    handlers=[      # Logs go both to file & console
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger") # will import it later using from src.datascience import logger

'''result in
logger.debug("Debug details")      # Won’t show
logger.info("Info message")        # Will show
logger.warning("Something odd")    # Will show
logger.error("An error happened")  # Will show
logger.critical("System down!")    # Will show
'''
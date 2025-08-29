# Import Path from pathlib to handle file system paths (cross-platform)
from pathlib import Path

# Import Python's built-in logging module for creating logs
import logging

# Import datetime to generate timestamped log filenames
from datetime import datetime


# ------------------ LOG FILE SETUP ------------------

# Create a log file name with the current date and time
# Example: "08_29_2025_09_15_30.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Get the current working directory where the script is running
cwd = Path.cwd()


# Define the full path for logs folder + log file
# Example: "C:/Users/YourName/Project/logs/08_29_2025_09_15_30.log"
log_path = cwd / "logs" / LOG_FILE


# Create the parent directory "logs" if it doesn’t already exist
# parents=True → creates all missing folders in the path
# exist_ok=True → prevents error if the folder already exists
log_path.parent.mkdir(parents=True, exist_ok=True)


# Create the empty log file if it doesn’t exist yet
# (just touches the file, doesn’t write anything yet)
log_path.touch(exist_ok=True)


# ------------------ LOGGING CONFIGURATION ------------------
logging.basicConfig(
  filename=log_path, # Save logs to the file path we built above
  format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
  # Log format explanation:
  #   %(asctime)s   → timestamp (with milliseconds by default)
  #   %(name)s      → logger name (usually 'root' if not custom)
  #   %(levelname)s → log severity level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  #   %(message)s   → actual log message text
  level=logging.DEBUG,   # Minimum log level → DEBUG (captures everything)
)

# So what does level=logging.DEBUG mean?

# It sets the minimum severity level for the logger.
# If you set it to DEBUG, all logs (DEBUG, INFO, WARNING, ERROR, CRITICAL) will be recorded.
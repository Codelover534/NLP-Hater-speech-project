from pathlib import Path
import logging

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# current working directory
cwd = Path.cwd()

log_path = cwd / "logs" / LOG_FILE
log_path.parent.mkdir(parents=True, exist_ok=True)
log_path.touch(exist_ok=True)

#levelnames severity (DEBUG < INFO < WARNING < ERROR < CRITICAL)
logging.basicConfig(
  filename=log_path,
  format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
  level=logging.DEBUG,
)

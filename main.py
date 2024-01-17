import sys
from pathlib import Path
current_directory = Path(__file__).parent
sys.path.append(str(current_directory / "configs"))
sys.path.append(str(current_directory / "logger"))

from logger import app_logger

if __name__ == '__main__':
    app_logger.info("info message")
    app_logger.debug("debug message")
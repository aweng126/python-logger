
# use virtual python environment
## create virtural environment
```
python3 -m venv .venv
```
## activate virtual environment
```
source ./venv/bin/activate
```
## deacticate virtual environment
```
deactivate
```

# install depencies
```
pip3 install -r requirements
```

# how to use the python-logger
## easy-test
```
# add the logger module and configs module into python path 
import sys
from pathlib import Path
current_directory = Path(__file__).parent
sys.path.append(str(current_directory / "configs"))
sys.path.append(str(current_directory / "logger"))

# import logger object from app_logger.py in logger module.
from logger import app_logger

if __name__ == '__main__':
    # just use it.
    app_logger.info("info message")
    app_logger.debug("debug message")
```

if you want to make your own python-logger. 
you can learn the configure in logger/logging_config.yaml. 


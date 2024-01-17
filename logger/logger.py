import os
import yaml
import logging.config
import app_config

def setup_logger(log_env:str):
    
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to the logging configuration file
    config_path = os.path.join(current_dir, 'logging_config.yaml')

    # Load the config file    
    with open(config_path, 'rt') as f:
        mconfig = yaml.safe_load(f.read())

    # Configure the logging module with the config file
    logging.config.dictConfig(mconfig)

    # Get a logger object
    if log_env == "development":
        return logging.getLogger('development')
    elif log_env == "staging":
        return logging.getLogger('staging')
    elif log_env == "production":
        return logging.getLogger('production')
    else:
        return None

app_logger = setup_logger(app_config.log_env)

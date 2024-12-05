# src/logger.py
import logging

def setup_logger(log_level=logging.INFO):
    # Create a logger
    logger = logging.getLogger("Codebasics_QA")
    logger.setLevel(log_level)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create formatter and attach it to handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Attach handler to logger
    logger.addHandler(console_handler)

    return logger

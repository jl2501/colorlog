import logging
from .colorformatter import ColorFormatter

def getLogger(name=None, level=logging.DEBUG, **kwargs):
    '''
    Description:
        simple wrapper around logging.getLogger that creates a console handler and
        attaches the ColorFormatter as the default formatter for console logging

    Input:
        *args, **kwargs: passed directly to logging.getLogger() as is.
    '''
    logger = logging.getLogger(name, **kwargs)
    logger.setLevel(level)
    color_formatter = ColorFormatter()
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(color_formatter)
    logger.addHandler(console_handler)

    return logger


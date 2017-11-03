import logging
from colorlog import ColorFormatter

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
colored_formatter = ColorFormatter()
console_handler.setFormatter(colored_formatter)
logger.addHandler(console_handler)

logger.debug('test debug message')
logger.info('test info message')
logger.warning('test warning message')
logger.error('test error message')
logger.critical('test critical message')

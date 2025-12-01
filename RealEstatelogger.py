import logging

logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

if not logger.handlers:

    # Formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s:%(levelname)s:Function:%(funcName)s:%(message)s ,Logger:%(name)s'
    )
    
    simple_formatter = logging.Formatter('%(levelname)s:%(message)s')

    # File Handler
    file_handler = logging.FileHandler('RealState.logs')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)

    # Stream Handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(simple_formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

logger.propagate = False

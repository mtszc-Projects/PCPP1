import logging

# TODO: Logger object
logger = logging.getLogger()
hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.world')
recommended_logger = logging.getLogger(__name__)

# TODO: Logging levels
# logging.basicConfig()
#
# logger = logging.getLogger()
#
# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

# TODO: The setLevel method
# logging.basicConfig()
#
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
#
# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

# TODO: Basic configuration (part 1)
# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a')
#
# logger = logging.getLogger()
#
# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

# TODO: Basic configuration (part 2)
# FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
#
# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)
#
# logger = logging.getLogger()
#
# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

# TODO: FileHandler object
# logger = logging.getLogger(__name__)
#
# handler = logging.FileHandler('prod.log', mode='w')
# handler.setLevel(logging.CRITICAL)
#
# logger.addHandler(handler)
#
# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

# TODO: Formatter object
# FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
#
# logger = logging.getLogger(__name__)
#
# handler = logging.FileHandler('prod.log', mode='w')
# handler.setLevel(logging.CRITICAL)
#
# formatter = logging.Formatter(FORMAT)
# handler.setFormatter(formatter)
#
# logger.addHandler(handler)
#
# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

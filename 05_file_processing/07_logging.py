"""
4.2.1.1 LAB: logging – Lab 01
https://edube.org/learn/pcpp1-5/logging-lab-01
"""
import logging
from random import randint

FORMAT = '%(levelname)s - %(message)s'
# logging.basicConfig(level=logging.DEBUG, filename='battery_temperature.log', filemode='a', format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

temperatures = [randint(20, 40) for temp in range(60)]
for temperature in temperatures:
    if temperature < 20:
        logger.debug(f'{temperature}')
    elif temperature < 30:
        logger.info(f'{temperature}')
    elif 30 <= temperature <= 35:
        logger.warning(f'{temperature}')
    elif temperature > 35:
        logger.critical(f'{temperature}')

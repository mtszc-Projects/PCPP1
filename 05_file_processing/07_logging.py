"""
4.2.1.1 LAB: logging – Lab 01
https://edube.org/learn/pcpp1-5/logging-lab-01
It's likely that the temperature of your phone battery can get pretty high. Check if that’s true. Write a program that
will simulate the recording of battery temperatures with an interval of one minute. The simulation should contain 60
logs (the last hour).
To simulate temperatures, use one of the available random functions in Python. Temperatures should be drawn in the range
of 20–40 degrees Celsius, and then saved in the following format:
LEVEL_NAME – TEMPERATURE_IN_CELSIUS UNIT => DEBUG – 20 C
The drawn temperatures should be assigned to the appropriate level depending on their value:
DEBUG = TEMPERATURE_IN_CELSIUS < 20
WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
CRITICAL = TEMPERATURE_IN_CELSIUS > 35
Put all logs in the battery_temperature.log file. The task will be completed when you implement your own handler and
formatter.
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

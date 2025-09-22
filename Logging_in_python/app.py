import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"), ##FileHandler("app1.log"): Save logs to a file
        logging.StreamHandler() ##StreamHandler(): Also show logs in the console (terminal/Jupyter)
    ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Addition {a}+{b} = {result}")
    return result

def substract(a,b):
    result=a-b
    logger.debug(f"Substract {a}-{b} = {result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplying {a} x {b} = {result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Division {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Divide by zero")
        return None
    

add(10,16)
substract(15,10)
multiply(10,5)
divide(20,10)
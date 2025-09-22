from logger import logging

def add(a,b):

    logging.debug("addition operation is taking place")
    return a+b

logging.debug("Addittion function is called")
add(10,15)
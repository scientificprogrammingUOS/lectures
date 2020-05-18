import logging
def my_func():
    logging.warning('warning in func') 
    
logging.warning('warning outside func')
logging.info('Info outside func') 
my_func()
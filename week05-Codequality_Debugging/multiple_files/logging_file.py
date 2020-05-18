import argparse
import logging

def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', dest='loglevel', help='log-level for logging-module. one of [DEBUG, INFO, WARNING, ERROR, CRITICAL]', default='WARNING')
    return parser.parse_args()


def main():
    args = parse_command_line_args()
    setup_logging(args.loglevel)
    logging.warning('warning outside func')
    logging.info('Info outside func') 
    my_func()
    
    
def setup_logging(loglevel):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)
    
    
def my_func():
    logging.warning('warning in func') 
    


    
if __name__ == '__main__':
    main()
    

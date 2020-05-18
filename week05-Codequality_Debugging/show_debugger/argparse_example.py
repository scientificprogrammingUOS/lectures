import argparse


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Name of the file you want to want to transfer')
    parser.add_argument('-s', '--second-argument', dest='second_argument', help='TODO', default='')
    parser.add_argument('-v', '--verbose', default=False, help='If you want to be verbose', action='store_true')
    return parser.parse_args()


def main():
    args = parse_command_line_args()
    print("filename: ", args.filename)
    print("second arg:", args.second_argument)
    if args.verbose:
        print("I am so verbose!")

    
if __name__ == '__main__':
    main()
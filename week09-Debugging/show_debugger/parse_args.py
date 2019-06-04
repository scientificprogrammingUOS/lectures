import argparse

def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='help1')
    parser.add_argument('--arg2', help='help2', default="val_arg2")
    return parser.parse_args()


def main():
    args = parse_command_line_args()
    print('arg1:', args.arg1)
    print('arg2:', args.arg2)


if __name__ == '__main__':
    main()
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Parse command line arguments.')
    parser.add_argument('--input', help='Input file path')
    parser.add_argument('--output', help='Output file path')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    print(f'Input file: {args.input}')
    print(f'Output file: {args.output}')

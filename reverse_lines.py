import argparse
version = 1.0
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=argparse.FileType('r'), help= 'File to read')
    parser.add_argument('--limit', '-l', help='Limit the number of lines to read', type=int)
    parser.add_argument('--version', '-v', action='version', version=f'%(prog)s v{version}')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    lines = args.file.readlines()
    lines.reverse()
    if args.limit:
        lines = lines[:args.limit]
    for line in lines:
        print(line.strip()[::-1])
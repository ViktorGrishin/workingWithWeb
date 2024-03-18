import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*',
                    type=str)
args = parser.parse_args()
if args.arg:
    for s in args.arg:
        print(s)
else:
    print('no args')

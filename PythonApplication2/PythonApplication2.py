import argparse

parser = argparse.ArgumentParser(description='Description for program')

parser.add_argument('positional_argument', metavar='posarg', type=int, nargs=2,
                    help='explain message for parameter')

parser.add_argument('-s', '--sum', dest='sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.sum(args.positional_argument))
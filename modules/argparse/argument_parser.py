# used for more complex argument passing
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Prints "Hello World!',
    type=str,
    metavar='STRING',
    default='Hello World',
    required=True,  # forces the user to pass a value
    nargs='+',  # allows a list of arguments
)
args = parser.parse_args()

if args.basic is None:
    print('BASIC value not passed')
else:
    print(f'BASIC: {args.basic}')
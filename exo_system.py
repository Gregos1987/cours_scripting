import argparse

parser = argparse.ArgumentParser(
                    prog = 'Mon programme',
                    description = 'Ecrit dans un fichier souhaité',
                    )

parser.add_argument('filename')           # positional argument
parser.add_argument('-m', '--message')      # option that takes a value
parser.add_argument('-e', '--end')
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

args = parser.parse_args()
print(args.filename, args.message, args.end, args.verbose)




import argparse

parser = argparse.ArgumentParser(
    prog = 'mon_programme'
    description = 'Affichage emoji'
)

parser.add_argument('-n', '--nombre', default=5, choices=range(3,15))
args = parser.parse_args()

print(args.mon_programme)




#correction

import argparse

parser = argparse.ArgumentParser(
                    prog = 'Mon programme qui écrit un emoji',
                    description = 'Ecrit des emojis',
                    )

parser.add_argument('emoji')           # positional argument
parser.add_argument('-n', '--number',type=int, choices=range(3, 16), default=5)      # option that takes a value

args = parser.parse_args()
# print(args.emoji, args.number)

for i in range(args.number):
    print(args.emoji, end="")
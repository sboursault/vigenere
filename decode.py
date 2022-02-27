import vigenere
from os.path import join
from os import walk
import time

directory = 'encoded'
key = '1234'


def read_file(directory, filename):
    file_path = join(directory, filename)
    with open(file_path) as f:
        return f.read()


filenames = next(walk(directory), (None, None, []))[2]
teams = [f.rstrip('.txt') for f in filenames]

team = ''
while team not in teams:
    print('\nWhat is your team name ?')
    [print(f" - {team}") for team in teams]
    team = input("\nTeam name: ").lower()

encoded_message = read_file(directory, f"{team}.txt")

while True:

    print(f"\nWho is behind this code : {[encoded_message]} ?\n")

    user_input = input("Enter the secret key: ")

    if not user_input:
        user_input = '_'

    result = vigenere.decode(user_input, encoded_message)

    if result.startswith('___') and result.endswith('___'):
        print(f"\n\nDecoded message: {[result.strip('_')]}")
        time.sleep(2)
        print("\n   ☆彡(ノ^ ^)ノ   Looks good !!   ヘ(^ ^ヘ)☆彡\n")
        break
    else:
        print(f"\n\nDecoded message:  {[result]}")
        time.sleep(2)
        print("\nIt's probably not the right key !   ¯\\_( ツ )_/¯  \n")
        time.sleep(3)
        print("\nTry again...  \n")

import time
import sys


def update_progress(count, total):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('\r[%s] %s%s' % (bar, percents, '%'))
    sys.stdout.flush()


def fake_progress():
    #for i in range(101):
    #    time.sleep(.07)
    #    update_progress(i, 100)
    time.sleep(1)


def vigenere_encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


def vigenere_decode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


encoded_message = "\x93\x96s¡\x96\x9c¤©T|\x9b£§«\x97\x9e¢\x96\x91"
key = "4725"

#print([vigenere_encode('4725', '__Albert Einstein__')])


while True:

    print(f"\nWho is behind this code : {[encoded_message]} ?\n")

    user_input = input("Enter the secret key: ")

    if not user_input:
        user_input = '_'

    fake_progress()

    result = vigenere_decode(user_input, encoded_message)

    if result.startswith('__') and result.endswith('__'):
        fake_progress()
        print(f"\n\nDecoded message: {[result.strip('_')]}")
        time.sleep(2)
        print("\n☆彡(ノ^ ^)ノ Looks good !! ヘ(^ ^ヘ)☆彡\n")
        break
    else:
        print(f"\n\nDecoded message:  {[result]}")
        time.sleep(2)
        print("\nIt's probably not the right key !   ¯\\_( ツ )_/¯  \n")
        time.sleep(4)
        print("\nTry again...  \n")

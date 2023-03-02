import time
from termcolor import colored
import os

import progress

os.system('clear')

expect = 'aze8'

while True:

    print("\nEntrez le code de dévérouillage: ")

    user_input = input('\n                             ')

    message = ''

    for i in range(0, len(user_input)):
        color = 'green' if user_input[i].lower() == expect[i] else 'red'
        message += ' ' + colored(user_input[i], color) + ' '

    print('\nVérification du code\n')

    progress.fake_progress(8)

    print('\n\n                         ' + message)

    time.sleep(1)

    if user_input.lower() == expect:
        print(colored('\n                     Procédure dévérouillée', 'blue'))

        launch = input("\nLancer la procédure de décollage ? (oui ou non) : ")
        if launch.strip().lower() == 'oui':
            time.sleep(1)
            print('\n                 ' + colored('Procédure de lancement engagée', 'yellow'))
            time.sleep(3)
            os.system(
                'vlc -f --play-and-exit --no-video-title-show --video-on-top countdown-and-rocket-launch.mp4')
        else:
            print('\n                       ' + colored('Procédure annulée', 'light_cyan'))

    else:
        print(colored('\n                   Ce n\'est pas le bon code', 'red'))
        time.sleep(1)

    print('\n--------------------------------------------------------------')





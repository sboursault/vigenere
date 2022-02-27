import vigenere
from os.path import join

messages = {
    "tatooine": {
        "message": "bonjour Jaba",
        "key": "1234"
    },
    "hoth": {
        "message": "glagla",
        "key": "5678"
    }
}


def write_file(directory, filename, content):
    file_path = join(directory, filename)
    with open(file_path, 'w') as f:
        f.write(content)


for team in messages:
    key = messages[team]['key']
    message = messages[team]['message']
    encoded_message = vigenere.encode(key, f"___{message}___")
    write_file('encoded', f'{team}.txt', encoded_message)

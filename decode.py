import vigenere

encoded_file = 'encoded/tatooine.txt'
key = '123'


with open(encoded_file) as f:
    encoded_message = f.read()

decoded_message = vigenere.decode(key, encoded_message)

print(decoded_message)

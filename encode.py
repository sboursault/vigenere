import vigenere

encoded_file = 'encoded/tatooine.txt'
message = "bonjour"
key = '123'


encoded_message = vigenere.encode(key, message)

with open(encoded_file, 'w') as f:
    f.write(encoded_message)

alphabet = " abcdefghijklmnopqrstuvwxyzABSCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,;:!?./§-_&"


def validate(input: str):
    for i in range(len(input)):
        if (input[i] not in alphabet):
            raise Exception(f"Unsupported character: '{input[i]}'")


def encode(key: str, message: str) -> str:
    key = normalize(key)
    message = normalize(message)
    encoded_chars = []
    validate(key)
    validate(message)
    for i in range(len(message)):
        key_c = key[i % len(key)]
        encoded_c = alphabet[(alphabet.index(message[i]) + alphabet.index(key_c)) % len(alphabet)]
        encoded_chars.append(encoded_c)
    return ''.join(encoded_chars)


def decode(key: str, encoded: str) -> str:
    key = normalize(key)
    encoded = normalize(encoded)
    encoded_chars = []
    for i in range(len(encoded)):
        key_c = key[i % len(key)]
        encoded_c = alphabet[(alphabet.index(encoded[i]) - alphabet.index(key_c)) % len(alphabet)]
        encoded_chars.append(encoded_c)
    return ''.join(encoded_chars)


def normalize(key):
    if len(key) == 0:
        key = ' '
    return key


# test = encode("7895", "voisdffg777``la voila")
# print(test)
# print(decode("7895", test))

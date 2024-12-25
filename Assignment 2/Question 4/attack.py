from decrypt import check_padding
from encrypt import encrypt
"""
You can implement helper function here if you want
"""

def get_padding(cipher_text):
    padding = 1
    while padding < 16:
        store = cipher_text[padding]
        cipher_text[padding] = store ^ 1
        ret = check_padding(cipher_text)
        if ret == 0:
            cipher_text[padding] = store
            break
        cipher_text[padding] = store
        padding += 1
    return padding

def attack(cipher_text):
    """
    Takes a ciphertext (list of integers from 0 to 255 [byte array]) as input
    TODO: Implement your code below
    """

    padding = get_padding(cipher_text)
    original_message = []
    print(padding)
    # print ("nice")
    print(len(cipher_text))
    while len(cipher_text) > 16:
        for i in range(padding , 16):

            for j in range(0,i):
                cipher_text[j] = cipher_text[j] ^ (i+1) ^ i
            for j in range(255 , -1 , -1):
                cipher_text[i] = cipher_text[i] ^ j
                ret = check_padding(cipher_text)
                if ret == 0:
                    original_message.append((i+1) ^ j)
                    break
                cipher_text[i] = cipher_text[i] ^ j
        cipher_text = cipher_text[16:]
        padding = 0

    """
    Return a list of integers representing the original message
    """
    return original_message

# message = [3 for i in range(16)]
# print(attack(encrypt(message)))
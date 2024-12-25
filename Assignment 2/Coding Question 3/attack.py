"""
You can implement helper function here if you want
"""

import decrypt

def attack(ciphertext, decrypt):
    """
    You are given a ciphertext(byte array) of size 48 on some random message of size 48 bytes. 
    You are also given access to the decryption function which takes a ciphertext of size 48 and outputs 48 bytes message corresponding to the ciphertext
    Example Use: decrypt(ciphertext)

    NOTE: 
        1. Ensure that ciphertext send as input to decrypt function is byte array of size 48
        2. Only one query can be made to decrypt function

    TODO: Implement your code below
    """

    ct1 = ciphertext[:16]
    ct2 = ciphertext[16:32]
    ct3 = ciphertext[32:]

    input = ct1 + ct2 + ct1
    # print(input)
    output = decrypt(input)

    pt1 = output[:16]
    pt2 = output[16:32]
    pt3 = output[32:]

    intpt1 = int.from_bytes(pt1, byteorder='big')
    intpt3 = int.from_bytes(pt3, byteorder='big')
    intct2 = int.from_bytes(ct2, byteorder='big')

    intkey = (intpt1 ^ intpt3 ^ intct2)
    key = intkey.to_bytes(16, byteorder='big')

    """
    Return the key in byte format
    Example of key: b'\xb8\x15\xd4\xeeUO\xdf\xa3\x02\xe9\x8d.\xb2\x10\xfa\x0c'
    """
    return key

# decrypt_obj = decrypt.decryption_oracle()
# print(attack(b'\x00'*48, decrypt_obj.decrypt))
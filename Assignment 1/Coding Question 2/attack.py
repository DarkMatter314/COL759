from des import encrypt, decrypt, key_gen

"""
You can implement helper function here if you want
"""

def attack(message, ciphertext):
    """
    TODO: Implement your code here, You can use encrypt, decrypt and key_gen functions for your attack
    """
    
    """
    Return the keys (k1, k2) such that ct = Enc(Enc(m, k1), k2) [ordering of keys matter]
    """
    intermediate = {}
    for i in range(0, 1<<20):
        key = key_gen(i)
        inter_ct = encrypt(key, message)
        intermediate[inter_ct] = key
    for i in range(0, 1<<20):
        key = key_gen(i)
        inter_msg = decrypt(key, ciphertext)
        if inter_msg in intermediate:
            return (intermediate[inter_msg], key)
    return None

# msg = input()
# key1 = key_gen(int(input()))
# key2 = key_gen(int(input()))
# print(f"Key1 : {key1} | Key2 : {key2}")
# print(attack(msg, encrypt(key2, encrypt(key1, msg))))
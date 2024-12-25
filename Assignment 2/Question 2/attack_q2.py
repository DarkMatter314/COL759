"""
write helper functions below if required
"""

def predict(permute, inverse_permute):
    """
    The challenger has sampled a bit b <- {0, 1} uniformly randomly:
        If b = 0, the challenger has chosen the Luby Rackoff Permutation
        If b = 1, the challenger has chosen a uniformly random permutation
    The permutation is over the space of strings of length 32 bytes, with key space over 3*128 bit keys

    Your goal is to predict the bit b that the challenger has sampled

    The given functions are simulating interacting with a challenger which has previously sampled a random bit b and a uniformly random key over the key space
        1. permute(x) - returns the permutation of x where x is of type bytes and len(x) = 32
        2. inverse_permute(x) - returns the inverse permutation of x where x is of type bytes and len(x) = 32

    NOTE: 
        1. Ensure that x is of type bytes and len(x) = 32 for both permute and inverse_permute
        2. A maximum of 8 queries can be made in total (combining both permute and inverse_permute)
        3. For at most 4 queries, full score will be awarded
        4. For at most 6 queries, 90% of the score will be awarded
        5. For at most 8 queries, 80% of the score will be awarded
        6. For more than 8 queries, 0% of the score will be awarded

    TODO: write your code below
    """
    # First we get the inverse of the permutation of 0
    input1 = (0).to_bytes(32, byteorder='big')  # 32 bytes of 0
    dec1 = inverse_permute(input1)  # we get (a || b)
    # Then we will permute 0 || a
    a = dec1[:16]  # a
    b = dec1[16:]  # b
    input2 = a + (0).to_bytes(16, byteorder='big')  # 16 bytes of a || 0
    dec2 = permute(input2)  # we get (c || d)
    # Now we will find inverse permutation of b XOR d || c
    c = dec2[:16]  # c
    d = dec2[16:]  # d
    # We will find inverse permutation of b XOR d || c

    input3 = c + bytes(x^y for x,y in zip(b,d))  # c || b XOR d
    dec3 = inverse_permute(input3)  # we get (e || f)

    # if e = c xor a  return 1
    # else return 0
    if dec3[:16] == bytes(x^y for x,y in zip(a,c)):
        return 0
    else:
        return 1



    """
    Return guess of b (either 0 or 1)
    """


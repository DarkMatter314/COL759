"""
You can define helper function here if you want
"""
import random

def bit_k(n,k):
    return ((n & (1<<(k))) >> (k))

def help(sig, msg):
    N = 1 << 2048
    padded = pow(sig, 3, N)
    # padded_bin = "1" + "0"*2000+"00000000101010101010101010101010"
    padded_bin = bin(padded)[2:]
    if not padded_bin.endswith("00000000"+bin(msg)[2:]): # check right part == 0x00 msg
        return -1
    if len(padded_bin) != 2033: # check left part == 0x00 0x01
        return -2
    rpad_len = (len(bin(msg))+6)//8
    for i in range(0, 254-rpad_len): # check for 0x00 in between
        if padded_bin[1+i*8:9+i*8] == "00000000":
            return 1
    return 2

def attack(N, e, msg):
    """
    write the code below
    """
    #2^676 2 ^ 677

    # target = "0x00" + hex(msg)[2:]
    # target = bin(int(target , 16))[2:]

    str_msg = str(bin(msg))
    target = "00000000" + str_msg[2::]
    s =  1
    c = 1
    #match bits between c and target from right to left
    #if mismatch, flip the bit in s
    #repeat until match
    #repeat for 1000 times
    # print(target)
    for i in range (1, len(target)):
        curr_bit = bit_k(c, i)  
        if (curr_bit != int(target[-(i+1)])):
            s += (1<<(i))
            c = pow(s, 3)
            # if help(c, msg) == 2:
            #     return s

    len1 = len(bin(s)) -2    
    s += (1<<(676))
    s += 1<<(677)
    c = pow(s, 3)



    for i in range(0,2500):
        s1 = random.getrandbits(674-len1)
        s2 = s + (s1<<(len1))
        if help(s2, msg) == 2:
            return s2
    
    return s


# print(attack(0,0,0b1010101010101010101010101010101010101010101010101010101010101010))

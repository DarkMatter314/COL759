from mrsa import dec, restart_system
import math


def attack():
    """
    Function details:
    restart_system(): It will return ((N, e), ct) where (N, e) is the public key and ct is the ciphertext you have to decrypt
        - You can call it maximum of 200 times
    dec(ct, N, d): It will return message corresponding to the given ciphertext ct using N and d
    """
   

    """
    return the message corresponding to the ciphertext you got from restart_sytem
    """


    i = 0
    N_seen = []
    while i < 200:
        ((N, e), ct) = restart_system()
        for n in N_seen:
            p = math.gcd(N, n)
            if p != 1:
                q = N//p
                d = pow(e, -1, (p-1)*(q-1))
                return dec(ct, N, d)
        N_seen.append(N)
        i += 1
    return None
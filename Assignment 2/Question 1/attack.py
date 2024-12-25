"""
You can implement helper function here if you want
"""

def solveKey(a1, a2, a3, b1, b2, b3, pi_func, p):
    k1 = ((a3*b1 - a1*b3) * pi_func(a2*b3 - a3*b2) ) % p
    k2 = ((a2*b1 - a1*b2) * pi_func(a3*b2 - a2*b3) ) % p
    return (k1, k2)

def attack(oracle, pi_func, p):
    """
    The challenger has sampled a bit b <- {0, 1} uniformly randomly:
        If b = 0, the challenger has chosen the PRP
        If b = 1, the challenger has chosen a uniformly random permutation

    Your goal is to predict the bit b that the challenger has sampled given access to p, the public permutation pi(x) used in PRP construction and oracle function

    The oracle function is simulating interacting with a challenger which has previously sampled a random bit b and two uniformly random keys k1 and k2 over the key space
        oracle(x) - returns the output on x where x is from 0 to p-1

    NOTE: 
        1. Ensure that x is from 0 to p-1
        2. A maximum of 5 queries can be made to oracle function
        3. You can make as many query as you want to the pi_func function
        4. For at most 3 queries to oracle, full score will be awarded
        5. For making 4 queries to oracle, 90% of the score will be awarded
        6. For making 5 queries to oracle, 85% of the score will be awarded

    TODO: Implement your code below
    """
    x1,x2,x3 = 0,1,2
    y1,y2,y3 = oracle(x1), oracle(x2), oracle(x3)
    a1 = x2*y2 - x1*y1
    a2 = y2-y1
    a3 = x1-x2
    b1 = x3*y3 - x1*y1
    b2 = y3-y1
    b3 = x1-x3
    k1,k2 = solveKey(a1, a2, a3, b1, b2, b3, pi_func, p)
    c1 = (x1 + k1)*(y1 - k2) % p
    c2 = (x2 + k1)*(y2 - k2) % p
    c3 = (x3 + k1)*(y3 - k2) % p
    if(c1 == 1 and c2 == 1 and c3 == 1): return 0
    else: return 1

    """
    Return guess of b (either 0 or 1)
    """
    return None
from rsa import check_padding,pad,encryption,get_key,bytes_to_num,num_to_bytes, KEY_FILE

def find_si(c, e, n , lower_bound):
    s_i = lower_bound
    while True:
        c0_si = pow(s_i, e, n) * c % n
        if check_padding(list(num_to_bytes(c0_si))):
            return s_i
        s_i += 1

def search_one_interval(a, b, N, e, c, s, B):
    r = 2*((b * s - 2 * B) // N)
    while True:
        lb = (2*B + r*N) // b
        ub = (3*B + r*N) // a
        for s in range(lb, ub + 1):
            new_c = (c * pow(s, e, N)) % N
            if check_padding(list(num_to_bytes(new_c))):
                return s
        r += 1

def narrow_set_of_solutions(previous_intervals, s_i, B, n):
    new_intervals = set()
    for interval in previous_intervals:
        a, b = interval
        lb = (a*s_i - 3*B + 1) // n
        ub = (b*s_i - 2*B) // n + 1
        for r in range (lb , ub +1):
            new_a = max(a, (2*B + r*n ) // s_i + 1)
            new_b = min(b, (3*B - 1 + r*n) // s_i)
            if new_a <= new_b:
                new_interval = (new_a, new_b)
                new_intervals.add(new_interval)
    return new_intervals

def search(N, e, c):
    k = (N.bit_length() + 7) // 8
    B = 2 ** (8 * (k - 2))
    intervals = set()
    intervals.add((2 * B, 3 * B - 1))
    s = N // (3 * B)
    s = find_si(c, e, N, s)
    while True:
        intervals = narrow_set_of_solutions(intervals, s, B, N)
        # print(f"Found valid s_i: {s} | Length of intervals: {len(intervals)}")
        if len(intervals) == 1:
            (a, b) = intervals.pop()
            intervals.add((a, b))
            if a == b:
                return a
            s = search_one_interval(a, b, N, e, c, s, B)
        else:
            s = find_si(c, e, N, s + 1)

"""
Takes a ciphertext, public modulus and public exponent as input as input
PARAMS:
ciphertext: a list of integers of size 128 bytes
N: the public modulus of size 128 bytes
e: the public exponent
"""
def attack(cipher_text, N, e):
    """
    TODO: Implement your code here
    """
    c = bytes_to_num(cipher_text)
    msg = search(N, e, c)
    msg = list(num_to_bytes(msg))[2:]
    for i in range(len(msg)):
        if msg[i] == 0:
            msg = msg[i+1:]
            break
    # print(f"Found message: {msg}")
    return msg
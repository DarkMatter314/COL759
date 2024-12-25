from encrypt import encrypt

"""
You can implement helper function here if you want
"""

def attack():
    """
    TODO: Implement your code here, You can use encrypt or decrypt or both function for your attack
    """

    cookie = ""
    temp = ""
    for _ in range (0,24):
        
        minchar = 'a'
        minlen = len(encrypt((temp +  minchar)))

        for i in range (0,26):
            if(len(encrypt(temp + chr(97+i)))  <= minlen):
                minchar = chr(97+i)
                minlen = len(encrypt((temp + chr(97+i))))
            
        count = 0
        
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if(len(encrypt(temp + letter))  == minlen):
                count += 1
        
        #if count is 1 then we have found the correct character
        #There are some cases where even if message contains substring of cookie the compression will be of bigger size
        # we found one such case where cookie was "aaaaaaaaaaaaaaaaaaaaaaaa" and after 16 bits it was giving same length for all characters
        # so to handle such we remove starting bits of our temporary string and and do the same again until we get count as 1
        #We can do this beacuse we know that the removed characters are 100% correct nad stored in final answer.


        while (count != 1):
            temp = temp[1:]
            minchar = 'a'
            minlen = len(encrypt((temp +  minchar)))
            for i in range (0,26):
                if(len(encrypt(temp + chr(97+i)))  <= minlen):
                    minchar = chr(97+i)
                    minlen = len(encrypt((temp + chr(97+i))))
                
            count = 0
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if(len(encrypt(temp + letter))  == minlen):
                    count += 1

        
        
        temp = temp + minchar
        cookie = cookie + minchar
        
    """
    Return the secret
    """
    return cookie

if __name__ == "__main__":
    print(attack())
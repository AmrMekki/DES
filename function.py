def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
    

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
    
    # Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
# ascii 
# A = 65
# Z = 90
# a = 97
# z = 122


"""
This function takes a string (ie. "AAAAA") which will be used in the other code
and splits into indiviudal character and increment by one ascii code.
So string_increment_by_one ("AAAAA") should give "BBBBB"
It assumes that A precedes a given their unicode value.
It wraps around so 'Z'  becomes 'a'
and 'z' becomes 'A'
Since this function is tailor made fo the geni project which uses 5 character password,
it wraps whole 5 characters accordingly so ("ZZZZZ" should become 'aaaaaa')
Once it gets to 'zzzzz' it should return -1 to indicate there cannot be more cases
"""
def string_increment_by_one (x):
    tokens = list(x)
    a = tokens[0]
    b = tokens[1]
    c = tokens[2]
    d = tokens[3]
    e = tokens[4]

    e = chr(ord(e) + 1)
    #check if last chr is Z then turn it into z
    if (ord(e) == 91):
        e = chr(ord(e) + 6)
    if (ord(e) == 123):
        e = chr(ord(e) - 58)
        d = chr(ord(d) + 1)
        if (ord(d) == 91 or ord(d) == 123):
            if (ord(d) == 91):
                d = chr(ord(d) + 6)
            if (ord(d) == 123):
                d = chr(ord(d) - 58)
                c = chr(ord(c) + 1)
                if (ord(c) == 91 or ord(c) == 123):
                    if (ord(c) == 91):
                        c = chr(ord(c) + 6)
                    if (ord(c) == 123):
                        c = chr(ord(c) - 58)
                        b = chr(ord(b) + 1)
                        if (ord(b) == 91 or ord(b) == 123):
                            if (ord(b) == 91):
                                b = chr(ord(b) + 6)
                            if (ord(b) == 123):
                                b = chr(ord(b) - 58)
                                a = chr(ord(a) + 1)
                                if (ord(a) == 91 or ord(a) == 123):
                                    if (ord(a) == 91):
                                        a = chr(ord(a) + 6)
                                    if (ord(a) == 123):
                                        return -1
    
    return str(a+b+c+d+e)

def test (x):
    while (True):
        result = string_increment_by_one (x)
        print(result)
        if (result == -1):
            break
        if (result == 'BBBBB'):
            break
        x = result
test('zyzzzz')
import codecs
import re


def encode(s):
    
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    s = s.ljust(1000, "p")
    for c in s:
        
        if c in digitmapping:
            crypted+=digitmapping[c]
        elif c.isalpha():
            if not re.match("[A-Za-z0-9_-]", c):
                raise ValueError
            elif c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c == " ":
            c.replace(" ", "")
        else:
            raise ValueError

    return crypted[:origlen]

def decode(s):
    if not isinstance(s,str):
        raise TypeError
    #if len(s) > 1000:
    #    raise ValueError
    #s = s.ljust(1000)
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            if c.isupper():
                c=c.lower()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError

    return crypted


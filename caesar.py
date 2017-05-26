import string

def change(ch,n):
    #print(type(ch))
    diff=26
    
    #if(type(ch) == int):
    if n<0:
        n=abs(n)%diff
        n=diff-abs(n)

    if chr(ch) in string.ascii_letters:
        if chr(ch) in string.ascii_uppercase:
            n=n%diff
            end=90-ch
                
            if end<n:
                ch=65+(n-end)-1
                return chr(ch)
            else:
                ch=ch+n
                return chr(ch)
        else:
            n=n%diff
            end=122-ch
            if end<n:
                ch=97+(n-end)-1
                return chr(ch)
            else:
                ch=ch+n
                return chr(ch)


def caesar(s,n):
    s = map(lambda ch:ord(ch) if ch in string.ascii_letters else ch, s)


    s = map(lambda ch:change(ch,n) if type(ch) == int else ch, s)
    s2="".join(s)
    return s2

print(caesar("zaxby4# kao",3))


def decrypt(s,n):
    return caesar(s,-n)

print(decrypt("Dove",3))



assert caesar("zaxby4# kao",3)=="cdaeb4# ndr", "Incorrect"
assert caesar("abc",2)=="cde","Incorrect"
assert caesar("abc",-2)=="yza","Incorrect"

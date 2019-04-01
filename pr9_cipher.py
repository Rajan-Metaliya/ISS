def gcd(a,b):
    if(a>b):
        a = a%b
    r1 = a
    r2 = b
    s1 = 1
    t1,s2,t2=1,0,0
    while(r2>0):
        print r1,r2,t1,t2
        q = r1/r2
        r = r1-q*r2
        r1,r2 = r2,r
        s = s1-q*s2
        s1,s2 = s2,s
        t = t1-q*t2
        t1,t2 = t2,t
    if t1<0:
        t1 = t1%b
    return t1
def affine_encipher(a,b,data):
    return [chr(65+(a*(ord(x)%32-1)+b)%26) for x in data]
def affine_decipher(a,b,data):
    print gcd(a,26)
    return [chr(65+(gcd(a,26)*((ord(x)%32-1)-b))%26) for x in data]
print affine_encipher(5,10,'bbbb')
print affine_decipher(5,10,affine_encipher(5,10,'bbbb'))
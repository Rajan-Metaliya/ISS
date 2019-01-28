def encrypt(data, key):
    key = (key*(len(data)/len(key)+1))[:len(data)]
    j=0
    str=""
    for i in data:
        temp = (ord(i))%32+(ord(key[j]))%32-1
        if(temp>26):
            temp = temp-26
            str+= chr(((ord(i))/32)*32+temp)
        else:
            str+=chr(ord(i)+ord(key[j])%32-1)
        j+=1
    return str
def decrypt(data,key):
    str=""
    key = (key * (len(data) / len(key) + 1))[:len(data)]
    j=0
    for i in data:
        temp = (ord(i))%32
        if(temp<=(ord(key[j])%32)):
            str+=chr(((ord(i))/32)*32+26-(ord(key[j])%32)+1+temp)
        else:
            str+=chr(ord(i)-ord(key[j])%32+1)
        j+=1
    return str

if __name__ == '__main__':
    data = raw_input("Please enter Plain text:")
    key = raw_input("Please enter Key:")
    print(encrypt(data,key))
    print(decrypt(encrypt(data,key),key))
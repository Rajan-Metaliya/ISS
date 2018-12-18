def encrypt(data,k):
    str =""
    temp =0
    for i in data:
        temp = (ord(i))%32+k
        print temp
        if(temp>26):
            temp = temp-26
            print temp
            print ((ord(i))/32)*32+temp
            str+= chr(((ord(i))/32)*32+temp)
        else:
            str+=chr(ord(i)+k)
    return str
def decrypt(data,k):
    str=""
    temp=0
    for i in data:
        temp = (ord(i))%32
        print temp
        if(temp<=k):
            str+=chr(((ord(i))/32)*32+26-k+temp)
        else:
            str+=chr(ord(i)-k)
    return str
if __name__ == "__main__":
    k = input("Please enter a key value: ")
    data = raw_input("Please enter data: ")
    str = encrypt(data,k)
    print(str,decrypt(str,k))

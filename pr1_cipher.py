def encrypt(data):
    str =""
    temp =0
    k=0
    for i in data:
        if i==" ":
            str+=i
            continue
        if ord(i)%2==0:
            k=1
        else:
            k=-1
        temp = (ord(i))%32+k
        print temp
        if(temp>26):
            temp = temp-26
            str+= chr(((ord(i))/32)*32+temp)
        elif(temp<=0):
            temp = temp+26
            str += chr(((ord(i)) / 32) * 32 + temp)
        else:
            str+=chr(ord(i)+k)
    return str
def decrypt(data):
    str=""
    temp=0
    k=0
    for i in data:
        if i==" ":
            str+=i
            continue
        if ord(i)%2==0:
            k=-1
        else:
            k=1
        temp = (ord(i))%32
        print temp
        if(temp>=26):
            str+=chr(((ord(i))/32)*32-k)
        elif(temp<=1):
            str+=chr(((ord(i)/32)*32)+26)
        else:
            str+=chr(ord(i)-k)
    return str
if __name__ == "__main__":
    #k = input("Please enter a key value: ")
    data = raw_input("Please enter data: ")
    str = encrypt(data)
    print(str,decrypt(str))

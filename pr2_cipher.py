def decrypt(data):
    str=""
    temp=0
    for k in range(1,26):
        str =""
        for i in data:
            temp = (ord(i))%32
            if(temp<=k):
                str+=chr(((ord(i))/32)*32+26-k+temp)
            else:
                str+=chr(ord(i)-k)
        print(str,k)

if __name__ == '__main__':
    li = ["PmttwEmtkwumBwCDXKM","Qefpfpzxbpbozfmeboxidlofqej","TrvjviTzgyvizjNvrbRcxfizkyd","LbhNerFzneggbNggnpxPnrfrePvcure"]
    for i in li:
        print("Decrypting for: "+ i)
        decrypt(i)
        print("=="*20)
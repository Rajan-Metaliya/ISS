import random


def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def Alice():
    global b,a,g,n
    x = random.randrange(1,100)
    print("x = "+ str(x))
    a = g**x % n
    Bob()
    print(str(a)+ " Alice")
    k1=b**x % n
    print("Alice Key = "+str(k1))
    print(encrypt("Hello",k1))

def Bob():
    global b, a, g, n
    y = random.randrange(1, 100)
    print("y = "+ str(y))
    b = g ** y % n
    print(str(b) + " Bob")
    k2 = a ** y % n
    print("Bob Key = "+str(k2))
    print(encrypt("Hello", k2))

g = int(input("Please enter G: "))
n = int(input("Please enter N: "))
a = None
b = None
Alice()
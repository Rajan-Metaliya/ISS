import math
import numpy as np
from numpy.linalg import inv, det

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1


def gen_matrix(string, rows, columns):
	return np.array([ord(i)-97 for i in list(string.lower())]).reshape(rows,columns)


def encrypt(msg, key):
	n = int(math.sqrt(len(key)))
	m = int(len(msg) / n)
	msg = gen_matrix(msg, n, m)
	key = gen_matrix(key, n, n)
	return "".join([chr(i+97) for i in np.dot(key, msg)%26])


def decrypt(msg, key):
	n = int(math.sqrt(len(key)))
	m = int(len(msg) / n)
	msg = gen_matrix(msg, n, m)
	key = gen_matrix(key, n, n)
	print(key)
	inverse = np.array([round(j) for i in inv(key)*det(key) for j in i]).reshape(n, n)
	inverse = (inverse*modInverse(det(key), 26)%26).astype(int)
	print(inverse)
	return "".join([chr(i[0]+97) for i in np.dot(inverse,msg)%26])

if __name__ == '__main__':
	msg = input("Enter a message: ")
	key = input("Enter key: ")
	cipher = encrypt(msg, key)
	print("Encrypted Msg: " + cipher)
	decipher = decrypt(cipher, key)
	print("Decrypted Msg: " + decipher)

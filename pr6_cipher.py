import numpy as np
import string
def gen_key(key,size):
    key_matrix = []
    if size==5:
        big_letters = list(string.ascii_lowercase)
        big_letters.remove('j')
    if size==6:
        big_letters = list(string.ascii_lowercase+"0123456789")
    for i in key:
        if i in big_letters:
            key_matrix.append(i)
            big_letters.remove(i)
    key_matrix = key_matrix+big_letters
    return np.array(key_matrix).reshape(size,size)
def encrypt(key,size,data):
    data_matrix = []
    out_data = []
    key_matrix = gen_key(key,size)
    print(key_matrix)
    cipher_data = ''
    data = ''.join(data.split())
    for i in range(0, len(data)):
        if i%2==0 and data[i]==data[i+1]:
            data = data[:i+1] + 'x' + data[i+1:]
    for i in range(0,len(data),2):
        data_matrix.append(list(data[i:i+2]))
    if len(data_matrix[-1])==1:
        data_matrix[-1].append('x')
    for i in data_matrix:
        n1,m1= np.where(key_matrix==i[0])
        n2,m2 = np.where(key_matrix==i[1])
        print('Found as:')
        print(key_matrix[n1,m1],key_matrix[n2,m2])
        if np.array_equal(n1,n2):
            if m1+1<size and m2+1<size:
                m1+=1
                m2+=1
            if m1+1>=size:
                m1=0
                m2+=1
            if m2+1>=size:
                m1+=1
                m2=0
        if np.array_equal(m1,m2):
            if n1+1<size and n2+1<size:
                n1+=1
                n2+=1
            if n1+1>=size:
                n1=0
                n2+=1
            if n2+1>=size:
                n2=0
                n1+=1
        if not np.array_equal(m1,m2) and not np.array_equal(n1,n2):
            m1,m2= m2,m1
        print('changed to')
        print(key_matrix[n1, m1],key_matrix[n2, m2])
        cipher_data+=str(key_matrix[n1, m1][0])+ str(key_matrix[n2, m2][0])
    return cipher_data
def decrypt(key,size,data):
     data_matrix = []
     cipher_data = ''
     out_data = []
     key_matrix = gen_key(key, size)
     data = ''.join(data.split())
     for i in range(0, len(data), 2):
         data_matrix.append(list(data[i:i + 2]))
     if len(data_matrix[-1]) == 1:
         data_matrix[-1].append('x')
     for i in data_matrix:
         n1, m1 = np.where(key_matrix == i[0])
         n2, m2 = np.where(key_matrix == i[1])
         print('Found as:')
         print(key_matrix[n1, m1], key_matrix[n2, m2])
         if np.array_equal(n1, n2):
             if m1 - 1 > 0  and m2 - 1 > 0:
                 m1 -= 1
                 m2 -= 1
             if m1 - 1 < 0:
                 m1 = [size-1]
                 m2 -= 1
             if m2 - 1 < 0:
                 m1 -= 1
                 m2 = [size-1]
         if np.array_equal(m1, m2):
             if n1 - 1 > 0 and n2 - 1 > 0:
                 n1 -= 1
                 n2 -= 1
             if n1 - 1 < 0:
                 n1 = [size-1]
                 n2 -= 1
             if n2 - 1 < 0:
                 n1 -= 1
                 n2 = [size-1]
         if not np.array_equal(m1, m2) and not np.array_equal(n1, n2):
             m1, m2 = m2, m1
         print('changed to')
         print(key_matrix[n1, m1], key_matrix[n2, m2])
         cipher_data += str(key_matrix[n1, m1][0]) + str(key_matrix[n2, m2][0])
     return cipher_data
a = encrypt("lilli",5,'heeeelo')
print('--------------------')
b = decrypt('lilli',5,a)
print('Encrypted:'+a+'\tDecrypted:'+b)

import random
def encrypt(key_dic,data):
    temp = ""
    for i in data:
        if i==" ":
            temp+=" "
            continue
        temp+=key_dic[i]
    return temp

def decrypt(key_dic,data):
    a = key_dic.values()
    b = key_dic.keys()
    key_dic = dict(zip(a,b))
    temp = ""
    for i in data:
        if i==" ":
            temp+=" "
            continue
        temp+=key_dic[i]
    return temp

def gen_key_dic():
    key_dic = {}
    key_lower = map(chr, range(ord('a'), ord('z')+1))
    value_lower = map(chr, range(ord('a'), ord('z')+1))
    key_upper = map(chr, range(ord('A'), ord('Z')+1))
    value_upper = map(chr, range(ord('A'), ord('Z')+1))
    for i in key_lower:
        ran = random.randint(0,len(value_lower)-1)
        key_dic[i] = value_lower[ran]
        value_lower.remove(key_dic[i])
    for i in key_upper:
        ran = random.randint(0,len(value_upper)-1)
        key_dic[i] = value_upper[ran]
        value_upper.remove(key_dic[i])
    return key_dic


if __name__ == '__main__':
    key_dic = gen_key_dic()
    print key_dic
    temp = encrypt(key_dic,"AA ZZ")
    print (temp,decrypt(key_dic,temp))
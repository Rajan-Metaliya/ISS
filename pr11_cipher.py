import random
def gen_k_m(n):
    n1 = n-1
    k = 1
    i =0
    while(n1%k==0):
        k*=2
        i+=1
    k/=2
    i-=1
    m = n1/k
    return k,i,m

def check_prime(n):
    a = random.randrange(1,n-1)
    k,i,m = gen_k_m(n)
    b = a**m %n
    if b==1 or b==-1 or b==n-1:
        print(str(n) +" is Prime Number")
        exit(0)
    if b!=1 or b!=-1:
        while(i>=0):
            b = b**2 % n
            i=i-1
            if b==-1 or b==n-1:
                print(str(n)+ " is Prime Number")
                exit(0)
            if b==1:
                print(str(n) + " is Composite Number")
                exit(0)
    print(str(n)+ " is Composite Number")

check_prime(17)
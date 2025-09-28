import random

def gcd(a, b):
    while b!=0:
        a, b=b, a%b
    return a
def is_prime_num(n):
        a=0
        for i in range(2,n):
            if n%i==0:
                a=1
        if a==1:
            print("plz enter \"prime number\".")
            return 0
        elif a==0:
            return 1
while True:
    p=int(input("Enter 1st prime number: "))
    if is_prime_num(p)==1:
        break
while True:
    q=int(input("Enter 2nd prime number: "))
    if is_prime_num(q)==1:
        if q==p:
            print("Can't use same prime number.")
        elif q*p<256:
            print("Can't use English string.")
            YN=input("(Yes/No): ")
            if YN in ["yes", "y", "Y", "YES", "Yes"]:
                break
            else:
                pass
        elif 255<q*p<55204:
            print("Can't use Korean string.")
            YN=input("(Yes/No): ")
            if YN in ["yes", "y", "Y", "YES", "Yes"]:
                break
            else:
                pass
        else:
            break
n=p*q
phi=(p-1)*(q-1)
eList=[]
while True:
    for i in range(1, phi):
        if gcd(i, phi) == 1:
            eList.append(i)
    break
#choose random e
e=random.choice(eList)
print(f"e is {e}")
#choose d
d=1
while True:
    if d*e%phi == 1:
        print(f"d is {d}")
        break
    d+=1
while True:
    M=input("Please enter the sentence you want to encrypt: ")
    Check_M=input("Are you going to use this sentence?(Y/N): ")
    if Check_M in ["yes", "y", "Y", "YES", "Yes"]:
        break
m_list=[]
for i in M:
    m=ord(i)
    m_list.append(m)

c_list=[]
for m in m_list:
    c=m**e%n
    c_list.append(c)
print(" encrypt: ", end="")
for i in c_list:
    c1=chr(i)
    print(c1, end="")
print("")

decryp_m=[]
for c in c_list:
    m=c**d%n
    decryp_m.append(m)
print(" decrypt: ", end="")
for i in decryp_m:
    m2=chr(i)
    print(m2, end="")
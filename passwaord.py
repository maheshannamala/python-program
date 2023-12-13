import random
l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=['1','2','3','4','5','6','7','8','9','10']
s=['@','$','%','&','#','^']
print("welcome to the password generator")
n0=int(input("how many letters you want in password "))
n1=int(input("how many symbols you want "))
n2=int(input("how many numbers you want "))
password =[]
for i in range(1,n0+1):
    password.append(random.choice(l))
for i in range(1,n1+1):
    password.append(random.choice(s))   
for i in range(1,n2+1):
    password.append(random.choice(n))  
print(password)
sum=""
for i in password:
    sum=sum+i   
print("your new password is ",str(sum))       
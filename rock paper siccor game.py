import random
a=int(input("what do you choose 0 for rock,1 for paper or 2 for scissors "))
r=random.randint(0,2)
print(f"computer choose {r}")
if(a==r):
    print("both are draw ")
elif(r==0 and a==1):
    print("you won")    
elif(r==1 and a==2):
    print("you won")
elif(r==2 and a==0):
    print("you won")   
elif(r==1 and a==0):  
    print("you lost compurer won")
elif(r==2 and a==1):
    print("you lost compurer won")
elif(r==0 and a==2):  
    print("you lost compurer won")             



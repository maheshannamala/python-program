def add(a,b):
    addition=a+b
    return float(addition)
def mul(a,b):
    multiply=a*b
    return float(multiply)
def sub(a,b):
    minus=a-b
    return float(minus)
def div(a,b):
    division=a/b
    return float(division)
def mod(a,b):
    modulus=a%b
    return float(modulus)
def calculator():
    operator={ "+":add,"-":sub,"x":mul,"/":div,"%":mod}                    
    type="Y"
    a=float(input("enter a number 1 "))
    while(type=="Y"):
     for i in operator:
         print(i)
     c=input("select the operator ")    
     b=float(input("enter a number2 "))
     func=operator[c]
     answer=func(a,b)
     print(answer)   
     type=input(f"press y for continue with {answer} and press n for terminate ").upper()   
     if(type=="Y"):
         a=answer
     else:
         type="N" 
         calculator()                 
calculator()
    
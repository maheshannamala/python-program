import random
from data import items
print("play the high lower game")
n=0
def game():
 global n
 r=random.choice(items)
 print("compare A:",r['name'], r['description'], r['country'])
 print("\nVS\n")
 r2=random.choice(items)
 if(r==r2):
     r2=random.choice(items)
 print("compare B:",r2['name'], r2['description'], r2['country'])
 a=input("who has more follower A or B ").upper()    
 if(a=="A"):
     if(r["follower_count"]>r2["follower_count"]):
          n=n+1
          print("you are correct your score ",n)
          game()   
     else:
         print("you are wrong total score ",n)      
 elif(a=="B"):
     if(r["follower_count"]<r2["follower_count"]):
         n=n+1
         print("you are correct your score ",n)
         game()
     else:     
         print("you are wrong total score ",n)         
game()     







import random
r=random.randint(1,101)
print("welcome to the number guessing game ")
print("thinking of number between 1 and 100 ")
n,n2=10,5
def difficulty():
  s=input("select the level you want to play 'easy' or 'hard' ").upper()
  if s=="EASY":
    return n
  else:
    return n2 
def guess():
 global n
 global n2
 turns=difficulty()
 print(f"you have {turns} attempts to guess the number ")
 g=int(input("guess the number "))
 for i in range(turns):
      if(g>r):
        print("too high")
      elif(g<r):
        print("too low")
      else:
        print(f"you guessed the correct number {r}")
        break
      turns-=1
      if(turns==0):
          print(f"game over actual number is {r}")
          break
      print(f"you have {turns} attempts to guess the number")
      g=int(input("guess the number "))                 
guess()   
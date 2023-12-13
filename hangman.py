import random
stages=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
 ''']
from words import word_list
live=7
chosen_word=random.choice(word_list)
display=[] 
for i in range(len(chosen_word)):
        display=display + list('_')
print(display) 
for j in range(len(chosen_word)):
             guess=input("guess a letter ").lower()
             for i in range(len(chosen_word)): 
                    letter=chosen_word[i]
                    if(letter==guess):
                        display[i]=letter
                        print(display)
             if guess not in chosen_word:
                 live-=1
                 print(stages[live])
                 print("you lost a chance")
                 if(live==0):
                   ("sorry lost")                                     
print(display)      
if '_' in display:
      print("you lose")
      print(f"actual word was {chosen_word} ")
else:
      print("you won")

         
        
       

        
       
from game_data import data
import random
from art import logo
from art import vs
import os
def comparision(r11,r22):
 if r11["follower_count"] > r22["follower_count"]:
  return 'A'
 elif r22["follower_count"] > r11["follower_count"]:
  return 'B'
def highgame():
  print(logo)
  r1 = random.choice(data)
  score = 0
  game_end = False
  while not game_end:
    print(f"Compare A: {r1['name']}, a {r1['description']}, from {r1['country']}.")
    print(vs)
    r2 = random.choice(data)
    print(f"Against B: {r2['name']}, a {r2['description']}, from {r2['country']}.")
    C = input("Who has more followers? Type 'A' or 'B': ")
    if C == comparision(r1,r2):
      if C == 'A':
       score += 1
       os.system('cls')
       print(f"Your current score = {score}")
      elif C == 'B':
       score += 1
       r1 = r2
       os.system('cls')
       print(f"Your current score = {score}")
    elif C != comparision(r1,r2):
     game_end = True
     os.system('cls')
     print(f"Sorry that's wrong. Final score ={score}")
     play_again = input("Do you want to play again?'Y' or 'N': ")
     if  play_again == 'Y':
      os.system('cls')
      highgame()
highgame()

  
  
  

     
   
    
    
   
   
   



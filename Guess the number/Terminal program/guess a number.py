
import random 
from art import logo
import os

def numbergame():
  number = str(random.randint(1,100))
  print(logo)
  print("Welcome to number guessing game")
  print("I'm thinking of a number between 1 and 100")
  easy_lives = 10
  hard_lives = 5
  print(f"pffft the number is {number}")
  difficulty = input("Choose difficulty level 'easy' or 'hard': ")
  endgame = False
  newgame = False
  
  if difficulty == "easy":
    print(f"You have {easy_lives} attempts remaining to guess the number")
  elif difficulty == "hard":
    print(f"You have {hard_lives} attempts remaining to guess the number")
    
  while not endgame:
    # userguess = input("Guess the number:")
    if difficulty == "easy" and easy_lives!=0 :
      userguess = input("Guess the number:")
      if userguess == number:
        print(f"Yay! You guessed it right. The number is {number} ")
        endgame = True
      elif userguess!= number:
        if userguess > number:
          print("Too high")
        elif userguess < number:
          print("Too low")
        easy_lives -= 1
        print(f"You have {easy_lives} attempts remaining to guess the number")
    elif easy_lives == 0 :
      print(f"You lost. The correct guess was {number}")
      endgame = True
      
    if difficulty == "hard" and hard_lives!=0:
      userguess = input("Guess the number:")
      if userguess == number:
        print(f"Yay! You guessed it right. The number is {number}")
        endgame = True
      elif userguess != number:
        if userguess > number:
          print("Too high")
        elif userguess < number:
          print("Too low")
        hard_lives -= 1
        print(f"You have {hard_lives} attempts remaining to guess the number")
    elif hard_lives == 0 :
      print(f"You lost. The correct guess was {number}")
      endgame = True
  if input("Do you want to play again type 'y' or 'n':") == "y":
    os.system('cls')
    numbergame()
  else:
    os.system('cls')

numbergame()


  
    





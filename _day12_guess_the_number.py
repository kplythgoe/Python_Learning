#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
logo = """
 _____                       _   _            _   _                 _               
|  __ \                     | | | |          | \ | |               | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|  
 
"""

print(logo)
print("Welcome to the number guessing game!\n")
print("I'm thinking of a number between 1 - 100")
random_number = random.randint(1,100)
print(f"psst, the correct answer is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives = 0
if difficulty == "easy":
  lives = 10
else:
  lives = 5

winner = False

while not winner:
  print(f"\nYou have {lives} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
  if guess != random_number:
    if guess > random_number:
      print("\nToo high")
    else:
      print("\nToo low")
    lives -= 1
    if lives == 0:
      print("You've run out of guesses, you lose")
      break
    print("Guess again")
    
  else:
    print(f"\nYou got it! The answer was {random_number}")
    winner = True



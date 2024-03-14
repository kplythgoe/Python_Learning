rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

userChoice = int(
    input(
        "What do you choose? Type 0 for rock, 1 for paper and 2 for scissors ")
)
computerChoice = random.randint(0, 2)
print("\n")
if userChoice == 0:
    print("You have chosen rock" + rock)
elif userChoice == 1:
    print("You have chosen paper" + paper)
elif userChoice == 2:
    print("You have chosen scissors" + scissors)
print("\n")
if computerChoice == 0:
    print("Your opponent has chosen rock" + rock)
elif computerChoice == 1:
    print("Your opponent has chosen paper" + paper)
else:
    print("Your opponent has chosen scissors" + scissors)

if (userChoice == 0 and computerChoice == 2) or (
        userChoice == 1 and computerChoice == 0) or (userChoice == 2
                                                     and computerChoice == 1):
    print("\nCongratulations, you win!")
elif userChoice == computerChoice:
    print("\n It's a draw!")
else:
    print("\nYou have lost. Better luck next time!")

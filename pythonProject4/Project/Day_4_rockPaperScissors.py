# Rock Paper Scissors ASCII Art
import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissor]

user_choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissor\n'))
print("User Choice: ")
print(options[user_choice])

print("Computer Choice")
computer_choice = random.randint(0,2)
print(options[computer_choice])

if user_choice == computer_choice:
    print("It's a Draw")
elif user_choice == 0 and computer_choice == 2:
    print("User Wins")
elif user_choice == 1 and computer_choice == 0:
    print("User Wins")
elif user_choice == 2 and computer_choice == 1:
    print("User Wins")
else:
    print("Computer Wins")

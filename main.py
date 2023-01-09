import random

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
options = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
  print("Invalid choice! You lose.")
else:
  print(options[user_choice])
  print("Computer chose:")
  computer_choice = random.randint(0, 2)
  print(options[computer_choice])
  
  if user_choice == 0 and computer_choice == 1: # rock vs paper
    print("You lose.")
  elif user_choice == 0 and computer_choice == 2: # rock vs scissors
    print("You win!")
  elif user_choice == 1 and computer_choice == 0: # paper vs rock
    print("You win!")
  elif user_choice == 1 and computer_choice == 2: # paper vs scissors
    print("You lose.")
  elif user_choice == 2 and computer_choice == 0: # scissors vs rock
    print("You lose.")
  elif user_choice == 2 and computer_choice == 1: # scissors vs paper
    print("You win!")
  else:
    print("It's a draw.")

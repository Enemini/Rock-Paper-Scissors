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

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if player_choice == 0:
  print(rock)
elif player_choice == 1:
  print(paper)
else:
  print(scissors)
  
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
  
if player_choice == computer_choice:
  print("It's a draw!")
elif (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1) or (player_choice == 0 and computer_choice == 2):
  print("Player won!")
else:
  print("Computer won!")
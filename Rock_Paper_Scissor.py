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

# Write your code below this line 👇

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissor: "))
system_choose = random.randint(0, 2)

print(f"system choose {system_choose} and user choose {user_choose}")


# -----------Rocks wins against Scissor---------------
if (user_choose == 0) and (system_choose == 2):
    print(f"You win {rock}")
elif system_choose == 0 and user_choose == 2:
    print(f"You lose {scissors}")
elif user_choose == system_choose:
    print("Drow the game!")
    
# ------------Scissor wins against Paper----------------
if (user_choose == 2) and (system_choose == 1):
    print(f'You win {scissors}')
elif (user_choose == 1) and (system_choose == 2):
    print(f'You lose {paper}')
elif (user_choose == system_choose):
    print("Drow the game!")
    
# ------------Paper wins against Rock-------------------
if (user_choose == 1) and (system_choose == 0):
    print(f'You win {paper}')
elif (user_choose == 0) and (system_choose == 1):
    print(f'You win {rock}')
elif (user_choose == system_choose):
    print("Drow the game!")

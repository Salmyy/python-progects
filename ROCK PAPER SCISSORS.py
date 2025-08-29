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

game_images=[rock,paper,scissors]

my_choice=int(input("choice 0 for rock , 1 for paper , 2 for scissors\n"))
if my_choice >= 0 and my_choice <=2:
   print(game_images[my_choice])

computer_choice=random.randint(0,2)
print(f"Computer choice:")
print(game_images[computer_choice])

if my_choice >= 3 or my_choice <0:
    print("You typed an invalid number.You lose! ")
elif my_choice == 0 and computer_choice ==2:
    print("You win!")
elif computer_choice==0 and my_choice==2:
    print("You lose!")
elif computer_choice >my_choice:
    print("You lose!")
elif my_choice >computer_choice:
    print("You win!")
elif computer_choice == my_choice:
    print("It< a draw!")

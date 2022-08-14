print("Welcome to the game")
import random
r = random.randint(1,101)
Guess = 1
while (Guess<=9):
    user = int(input("Enter Your Guess : "))
    if r > user:
       print("Please Enter a Bigger Number \n")
    elif r < user:
       print("Please Enter a Smaller Number \n")
    else:
       print("You Won")
       print("You took",Guess,"Number of guess to finish")
       break
    print(9-Guess,"Number of Guesses left \n")
    Guess = Guess+1    
if (Guess>9):
    print("Game Over")

    




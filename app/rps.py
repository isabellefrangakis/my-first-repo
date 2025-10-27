import random
VALID_OPTIONS = ["rock", "paper" , "scissors"]

# ASK USER FOR AN INPUT (R/P/S)

user_choice = input("Please choose one of the folowing 'rock', 'paper', or 'scissors'.")
print("USER:", user_choice)

# VALIDATIONS
if user_choice not in VALID_OPTIONS:
    print("OO{S INVALID INPUT, PLEASE TRY AGAIN")

# GENERATE RANDOM COMPUTER CHOICE
computer_choice = random.choice(VALID_OPTIONS)
print("COMP:", computer_choice)

# DETERMINE THE WINNER
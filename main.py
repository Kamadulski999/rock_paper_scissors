import random

while True:
    arr = ["Rock", "Paper", "Scissors"]
    guess = input('Rock, Paper, or Scissors? ').lower()
    if guess == 'rock' or guess == 'paper' or guess == 'scissors':
        comp_guess = arr[(random.randint(0, 2))]
        print("The computer's guess is " + comp_guess)
        if comp_guess.lower() == "rock" and guess == "paper":
            print("Paper beats Rock. You win. Congrats!")
            break
        if comp_guess.lower() == "rock" and guess == "scissors":
            print("Rock beats Scissors. Sorry. You lose!")
            break
        if comp_guess.lower() == "scissors" and guess == "rock":
            print("Rock beats Scissors. You win. Congrats!")
            break
        if comp_guess.lower() == "scissors" and guess == "paper":
            print("Scissors beats Paper. Sorry. You lose!")
            break
        if comp_guess.lower() == "paper" and guess == "rock":
            print("Paper beats Rock. You win. Congrats!")
            break
        if comp_guess.lower() == "paper" and guess == "scissors":
            print("Scissors beats Paper. Sorry. You lose!")
            break
        if comp_guess.lower() == guess:
            print("Tie. ")
    print("Please choose one of the options.")












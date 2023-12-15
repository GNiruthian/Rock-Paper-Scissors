import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: )")
    options = ["rock", "paper", "scissor"]
    computer_chocie = random.choice(options)
    choices = {"player": player_choice, "computer": computer_chocie}
    return choices

def check_win(player, computer):
    print("You chose" + player + ", computer chose" + computer)
    if player == computer:
        return "It's a Tie == !"

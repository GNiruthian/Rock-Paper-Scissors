import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors)")
    computer_chocie = "paper"
    choices = {"player": player_choice, "computer": computer_chocie}
    return choices

choices = get_choices()
print(choices)

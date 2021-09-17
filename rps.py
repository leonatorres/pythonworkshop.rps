import random 
def rps():
  while True:
    user_action = input("Enter a choice rock, paper, or scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_actions = random.choice(possible_actions)
    # \n new line
    print(f" you chose {user_action} , computer chose {computer_actions} .\n")

    #Tie
    if user_action == computer_actions:
      print(f"Both players selected {user_action} . It's a tie")

    # user rock
    elif user_action == "rock":
      if computer_actions == "scissors":
        print("Rock smashed scissors! You win!")
      else:
        print("Paper covers rock ... you lose ...")

    #user paper
    elif user_action == "paper":
      if computer_actions == "rock":
        print("Paper covers rock! You win!")
      else:
        print("Scissors cuts paper! ... you lose ...")

    # user scissors 
    elif user_action == "scissors":
      if computer_actions == "paper":
        print("Scissors cuts paper! You win!")
      else:
        print("Rock smashes scissors ... you lose ...")

    play_again = input("Play again? (y/n) ")
    if play_again.lower() != "y":       #lower.() if user put capital Y would revert it to lower case
      exit()

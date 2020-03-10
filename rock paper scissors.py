import random
def mega_start():
    while True:
        start = input("Do you want to play rock, paper, scissors? ")
        if start.lower() not in ["yes", "no"]:
            print("sorry, you should enter 'yes' or 'no'")
            continue
        else:
            break
    if start == "no":
        print("quitting game...")
        pass
    if start == "yes":
        print("starting game...")
        while True:
            computer = input("do you want to play against a computer? ")
            if computer.lower() not in ["yes", "no"]:
                print("sorry, you should enter 'yes' or 'no'")
            else:
                break
        if computer == "yes":
            def against_computer():
                p1_score = 0
                computer_score = 0
                computer_choices = ["rock", "paper", "scissors"]
                again = True
                while again:
                    while True:
                        super_player1 = input("Rock, paper or scissors? ")
                        if super_player1.lower() not in ["rock", "paper", "scissors"]:
                            print("sorry, invalid response")
                            continue
                        else:
                            break
                    computer_play = random.choice(computer_choices)
                    if super_player1 == computer_play:
                        print("it's a tie")
                    elif super_player1 == "rock":
                        if computer_play == "paper":
                            print("computer wins")
                            computer_score += 1
                        else:
                            print("you win!")
                            p1_score += 1
                    elif super_player1 == "paper":
                        if computer_play == "rock":
                            print("you win!")
                            p1_score += 1
                        else:
                            print("computer wins")
                            computer_score += 1
                    elif super_player1 == "scissors":
                        if computer_play == "rock":
                            print(f"computer wins")
                            computer_score += 1
                        else:
                            print("you win!")
                            p1_score += 1
                    print(f"your score: {p1_score}")
                    print(f"computer's score: {computer_score}")
                    while True:
                        play_again = input("do you want to play again? ")
                        if play_again.lower() not in ["yes", "no"]:
                            print("sorry, you should enter 'yes' or 'no'")
                        else:
                            break
                    if play_again == "no":
                        print("Thanks for playing!")
                        break
                    if play_again == "yes":
                        pass
            against_computer()
        if computer == "no":
            print("you will be playing against another player...")
            def rock_paper_scissors():
                p1_score = 0
                player1 = input("Hi what's your name? ")
                player2 = input("Hi, what's your name? ")
                p2_score = 0
                again = True
                while again:
                    while True:
                        super_player1 = input("rock, paper or scissors? ")
                        if super_player1.lower() not in ["rock", "paper", "scissors"]:
                            print("sorry, invalid response")
                            continue
                        else:
                            break
                    while True:
                        super_player2 = input("Rock, Paper or Scissors? ")
                        if super_player2.lower() not in ["rock", "paper", "scissors"]:
                            print("sorry, invalid response")
                            continue
                        else:
                            break
                    if super_player1 == super_player2:
                        print("it's a tie")
                    elif super_player1 == "rock":
                        if super_player2 == "paper":
                            print(f"{player2} wins!")
                            p2_score += 1
                        else:
                            print(f"{player1} wins!")
                            p1_score += 1
                    elif super_player1 == "paper":
                        if super_player2 == "rock":
                            print(f"{player1} wins!")
                            p1_score += 1
                        else:
                            print(f"{player2} wins!")
                            p2_score += 1
                    elif super_player1 == "scissors":
                        if super_player2 == "rock":
                            print(f"{player2} wins!")
                            p2_score += 1
                        else:
                            print(f"{player1} wins!")
                            p1_score += 1
                    print(f"{player1}'s score: {p1_score}")
                    print(f"{player2}'s score: {p2_score}")
                    while True:
                        play_again = input("do you want to play again? ")
                        if play_again.lower() not in ["yes", "no"]:
                            print("sorry, you should enter 'yes' or 'no'")
                        else:
                            break
                    if play_again == "no":
                        print("Thanks for playing!")
                        break
                    if play_again == "yes":
                        pass
            rock_paper_scissors()


mega_start()
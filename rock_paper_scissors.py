import random

def rock_paper_scissors():
    print("Let's play ROCK PAPER SCISSORS \n")

    r = "Rock"
    p = "Paper"
    s = "Scissors"

    y = (r, p, s)

    user = input(f"Enter any of these {r, p, s} : ")

    if user not in y:
        print("Invalid choice \n")
        return 

    computer = random.choice(y)
    print(f"You choose {user} and the computer choose {computer}")

    if user == computer:
        print("Game Tied !!")
    elif (
        (user == r and computer == s)
        or (user == p and computer == r)
        or (user == s and computer == p)
        ):
        print("You Win !!")
    else:
        print("You Loose !!")

rock_paper_scissors()


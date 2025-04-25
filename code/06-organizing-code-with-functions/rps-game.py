print("--------------------------")
print(" Rock Paper Scissors v1 ")
print("--------------------------")

player_1 = input("Enter player 1's name: ")
player_2 = input("Enter player 2's name: ")

rolls = ["rock","paper","scissors"]

roll_1 = input(f"{player_1} what is your roll ? {rolls}: ")
roll_1 = roll_1.lower().strip()
if roll_1 not in rolls:
    print(f"Sorry {player_1}, that is not a valid choice.")

roll_2 = input(f"{player_2} what is your roll ? {rolls}: ")
roll_2 = roll_2.lower().strip()
if roll_2 not in rolls:
    print(f"Sorry {player_2}, that is not a valid choice.")

print(f"{player_1} rolls {roll_1}.")
print(f"{player_2} rolls {roll_2}.")

# Test for a winner
winner = None

# Rock
#    Rock -> tie
#    Paper -> lose
#    Scissors -> win
# Paper
#    Rock -> win
#    Paper -> tie
#    Scissors -> lose
# Scissors
#    Rock -> lose
#    Paper -> win
#    Scissors -> tie

if roll_1 == roll_2:
    print("It's a tie!")
elif roll_1 == "rock":
    if roll_2 == "paper":
        winner = player_2
    elif roll_2 == "scissors":
        winner = player_1
elif roll_1 == "paper":
    if roll_2 == "scissors":
        winner = player_2
    elif roll_2 == "rock":
        winner = player_1
elif roll_1 == "scissors":
    if roll_2 == "rock":
        winner = player_2
    elif roll_2 == "paper":
        winner = player_1


print("The game is over!")
if winner is None:
    print("It was a tie!")
else:
    print(f"{winner} is the winner!")

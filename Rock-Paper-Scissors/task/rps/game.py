from random import choice

rating = open("rating.txt", 'r')

valid = []
loser_winner = {}


def make_list(x):
    global valid
    if x != "":
        valid = x.split(",")
    else:
        valid = ["rock", "paper", "scissors"]


def make_dict():
    global valid, loser_winner
    for i in valid:
        ind = valid.index(i)
        if ind < len(valid) / 2:
            loser_winner[i] = valid[ind + 1:ind + int(len(valid) / 2) + 1]
        else:
            loser_winner[i] = valid[ind + 1:] + valid[:int(len(valid) / 2) - (len(valid) - ind - 1)]


name = input("Enter your name: ")
print(f"Hello, {name}")
score = 0

input_list = input()
make_list(input_list)
make_dict()
print("Okay, let's start")

for line in rating:
    line_list = line.split(" ")
    if line_list[0] == name:
        score = int(line_list[1])

user_input = input()

while user_input != "!exit":
    computer_choice = choice(valid)
    if user_input == computer_choice:
        print("There is a draw ({})".format(user_input))
        score += 50
    elif user_input == "!rating":
        print("Your rating: " + str(score))
    elif user_input not in valid:
        print("Invalid input")
    elif computer_choice in loser_winner[user_input]:
        print("Sorry, but computer chose {}".format(computer_choice))
    elif computer_choice not in loser_winner[user_input]:
        print("Well done. Computer chose {} and failed".format(computer_choice))
        score += 100
    user_input = input()

print("Bye!")
rating.close()

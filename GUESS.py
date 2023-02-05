import random
number = random.randint(0,10)

player_name = input("Please enter your name : ")
no_of_guesses = 0

print("Okay" , player_name , "Please guess the number between 1 and 10")

while no_of_guesses < 5:
    guess = int(input())
    no_of_guesses += 1
    if guess < number:
        print("Guess is too low")
    if guess > number:
        print("Guess is too high")
    if guess == number:
        break

if guess==number:
    print("Well Done!! You guessed the number in ", str(no_of_guesses), "guesses")
else :
    print("Oh no!! The number was", str(number))

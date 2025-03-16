import random

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")
random_number = random.randint(1, 100)
difficulty = input('Choose a difficulty "Easy" or "Hard"')
print(difficulty)
print(random_number)

if difficulty == 'Easy':
    lives = 10
elif difficulty == 'Hard':
    lives = 5

GAME_OVER = False

while not GAME_OVER:

    print(f"You have {lives} attempts remaining to guess the number")
    user_input = int(input('Make a guess : '))
    if user_input == random_number:
        print("You guess it right")
        GAME_OVER = True
    elif user_input != random_number:
        lives -= 1
        if user_input > random_number:
            print('Provide input is greater than guessed number')
        elif user_input < random_number:
            print('Provided input is less than guessed number')

    if lives < 1:
        print("You ran out of lives")
        GAME_OVER = True

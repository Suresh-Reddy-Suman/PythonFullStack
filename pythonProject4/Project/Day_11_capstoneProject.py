import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
USER_CARDS = []
COMPUTER_CARDS = []
user_score = -1
computer_score = -1
GAME_OVER = False


def deal_card():
    """Return a random number or card from the list of cards dec"""
    return random.choice(CARDS)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == 0:
        print("User Wins")
    elif c_score == 0:
        print("Computer Wins")
    elif u_score > 21:
        print("Computer Wins")
    elif c_score > 21:
        print("User Wins")
    elif u_score == c_score:
        print("It's a Draw")
    elif u_score > c_score:
        print('User wins')
    else:
        print("Computer Wins")


for _ in range(2):
    USER_CARDS.append(deal_card())
    COMPUTER_CARDS.append(deal_card())

while not GAME_OVER:
    user_score = calculate_score(USER_CARDS)
    computer_score = calculate_score(COMPUTER_CARDS)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        print(user_score)
        GAME_OVER = True
    else:
        print(f"Your cards : {USER_CARDS}, current score : {user_score}")
        new_card = input("Do you want a new card? y or n")
        if new_card == 'y':
            USER_CARDS.append(deal_card())
        else:
            GAME_OVER = True

while computer_score != 0 and computer_score < 17:
    COMPUTER_CARDS.append(deal_card())
    computer_score = calculate_score(COMPUTER_CARDS)

print(f"Computer Cards : {COMPUTER_CARDS}, Computer Score : {computer_score}")
compare(user_score, computer_score)

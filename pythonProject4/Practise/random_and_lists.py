import random

friends = ["A", "B", "C", "D", "E"]

random_choice = random.randint(0,len(friends)-1)

print(f'{friends[random_choice]} is going to pay the bill')
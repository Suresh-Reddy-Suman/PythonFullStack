# def is_prime(num):
#     count = 0
#     for x in range(2, num + 1):
#         if num % x == 0:
#             count += 1
#
#     if count > 1:
#         print(f'{num} is not a prime number')
#         return False
#     else:
#         print(f'{num} is a prime number')
#         return True
#
#
# is_prime(11)

enemies = 2


def new_enemies():
    enemies = 3
    print(enemies)

new_enemies()
print(enemies)
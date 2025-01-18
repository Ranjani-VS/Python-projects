from Higherlowerart import *
import random
from HigherLowergame_data import *
def game1():
        return a["follower_count"]
def game2():
        return b["follower_count"]
print(logo)
score = 0
is_game=True

while is_game:

    a = random.choice(data)
    b = random.choice(data)

    print(f"Compare_A: {a["name"]}, {a["description"]}, from {a["country"]}")
    print(vs)
    print(f"Against_B: {b["name"]}, {b["description"]}, from {b["country"]}")

    c =game1()
    d =game2()
    e=c
    f=d
    user_inp = input("Who has more followers? Type 'A' or 'B':").lower()

    if user_inp=='a':
        if e>f:
            score=score+1
            print(f"You're right! Current score:{score}")
        else:
            print(f"Sorry, that's wrong. Final score:{score}")
            is_game = False
    elif user_inp=='b':
        if e<f:
            score=score+1
            print(f"You're right! Current score:{score}")
        else:
            print(f"Sorry, that's wrong. Final score:{score}")
            is_game = False



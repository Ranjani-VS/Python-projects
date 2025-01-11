S=15
M=20
L=25
pepperoni_for_small=2
pepperoni_for_me_la=3
extra_cheese=1
bill=0
print("Welcome to Python pizza deliveries:")
size=input("What size pizza do you want? S,M or L")
pepperoni=input("Do u want pepperoni on your pizza? Y or N")
extra=input("Do u want extra cheese? Y or N")
if size=='S':
    if pepperoni == 'Y':
        if extra == 'Y':
            bill=S + pepperoni_for_small + extra_cheese
            print(f"You bill is: {bill}")
        else:
            bill = S + pepperoni_for_small
            print(f"You bill is: {bill}")
    elif pepperoni == 'N':
            if extra=='Y':
                bill = S + extra_cheese
                print(f"You bill is: {bill}")
            else:
                bill = S
                print(f"You bill is: {bill}")
elif size=='M':
    if pepperoni == 'Y':
        if extra == 'Y':
            bill=M+pepperoni_for_me_la+extra_cheese
            print(f"You bill is: {bill}")
        else:
            bill = M + pepperoni_for_me_la
            print(f"You bill is: {bill}")
    elif pepperoni == 'N':
            if extra=='Y':
                bill = M + extra_cheese
                print(f"You bill is: {bill}")
            else:
                bill = M
                print(f"You bill is: {bill}")
elif size == 'L':
    if pepperoni == 'Y':
        if extra == 'Y':
            bill=L+pepperoni_for_me_la+extra_cheese
            print(f"You bill is: {bill}")
        else:
            bill = L + pepperoni_for_me_la
            print(f"You bill is: {bill}")
    elif pepperoni == 'N':
            if extra=='Y':
                bill = L + extra_cheese
                print(f"You bill is: {bill}")
            else:
                bill = L
                print(f"You bill is: {bill}")
else:
    print("Wrong input")
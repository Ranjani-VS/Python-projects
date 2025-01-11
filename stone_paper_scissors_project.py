import random
number=int(input("What do you choose?\nType 0 for rock\n1 for paper\n2 for scissors\n"))
co=[0,1,2]
computer=random.choice(co)


if number==0:
    print("you chose rock")
    print('''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''')
elif number==1:
    print("you chose paper")
    print('''
                _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)''')
elif number==2:
    print("you chose scissors")
    print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)''')
else:
    print("wrong input")
if computer==0:
    print("computer chose rock")
    print('''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''')
elif computer==1:
    print("computer chose paper")
    print('''
                _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)''')
elif computer==2:
    print("computer chose scissors")
    print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)''')
else:
    print("wrong input")
if number==0 and computer==1:
    print("you lose")
elif number==1 and computer==2:
    print("you lose")
elif number==2 and computer==0:
    print("you lose")
elif number==1 and computer==0:
    print("you win")
elif number==2 and computer==1:
    print("you win")
elif number==0 and computer==2:
    print("you win")
elif (number==0 and computer==0) or (number==1 and computer==1) or (number==2 and computer==2):
    print("Draw match")
logo='''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)
print("Calculator Program")
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={"+":add,"-":subtract,"*":multiply,"/":divide}
first=True
while first==True:
    result=True

    a=float(input("What's the first number?"))
    while result==True:
        for symbol in operations:
            print(symbol)
        r=input("Pick an operation:")
        c=float(input("What's the next number?"))
        answer=operations[r](a,c)
        print(f"{a}{r}{c}={answer}")
        cont=input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation:")
        if cont=="y":
            a=answer
        else:
            result=False
            print("\n" * 20)
import random


# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
se=[0,1,2]
b=1
# For user input
for i in range(0,3):          # A for loop for row entries
    a =[]
    for j in range(0,3):      # A for loop for column entries
         a.append("-")
    matrix.append(a)
b=1
for i in range(0,3):          # A for loop for row entries

    for j in range(0,3):      # A for loop for column entries

        if b%2==0:            # user's turn to play
                g=int(input("Enter the row number:"))
                h=int(input("Enter the column number"))
                print(f"Your row and column value in the matrix is:{g}{h}")
                if g<3 and h<3:
                    i=g
                    j=h
                    if matrix[i][j]=="-":
                        matrix[i][j]="o"
                        b=b+1
        else:                   # computer's turn to play
                l = random.choice(se)
                print(f"The computer's row value is:{l}")
                m = random.choice(se)
                print(f"The computer's column value is:{m}")
                i=l
                j=m
                print(f"Your row and column value in the matrix is:{l}{m}")
                if matrix[i][j] == "-":
                    matrix[i][j]="x"
                    b=b+1


        for row in matrix:
            y = 0
            for element in row:

                if y<2:
                    print(element, end=' | ')
                    y=y+1
                else:
                    print(element)
              # Move to the next line after printing each row
            print("----------")



    if matrix[0][0]=="o" and matrix[1][0]=="o" and matrix[2][0]=="o":
        print("you win")
        break
    elif matrix[0][0]=="x" and matrix[1][0]=="x" and matrix[2][0]=="x":
        print("computer wins")
        break
    elif matrix[0][1]=="o" and matrix[1][1]=="o" and matrix[2][1]=="o":
        print("you win")
        break
    elif matrix[0][1]=="x" and matrix[1][1]=="x" and matrix[2][1]=="x":
        print("computer wins")
        break
    elif matrix[0][2]=="o" and matrix[1][2]=="o" and matrix[2][2]=="o":
        print("you win")
        break
    elif matrix[0][2]=="x" and matrix[1][2]=="x" and matrix[2][2]=="x":
        print("computer wins")
        break
    elif matrix[0][0]=="o" and matrix[1][1]=="o" and matrix[2][2]=="o":
        print("you win")
        break
    elif matrix[0][0]=="x" and matrix[1][1]=="x" and matrix[2][2]=="x":
        print("computer wins")
        break
    elif matrix[0][2]=="o" and matrix[1][1]=="o" and matrix[2][0]=="o":
        print("you win")
        break
    elif matrix[0][2]=="x" and matrix[1][1]=="x" and matrix[2][0]=="x":
        print("computer wins")
        break
    elif matrix[0][0] == "o" and matrix[0][1] == "o" and matrix[0][2] == "o":
        print("you win")
        break
    elif matrix[0][0] == "x" and matrix[0][1] == "x" and matrix[0][2] == "x":
        print("computer wins")
        break
    elif matrix[1][0] == "o" and matrix[1][1] == "o" and matrix[1][2] == "o":
        print("you win")
        break
    elif matrix[1][0] == "x" and matrix[1][1] == "x" and matrix[1][2] == "x":
        print("computer wins")
        break
    elif matrix[2][0] == "o" and matrix[2][1] == "o" and matrix[2][2] == "o":
        print("you win")
        break
    elif matrix[2][0] == "x" and matrix[2][1] == "x" and matrix[2][2] == "x":
        print("computer wins")
        break






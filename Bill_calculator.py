print("Welcome to the tip calculator!")
total=float(input("What was the total bill?"))
tip=int(input("How much tip would you like to give? 10,12 or 15?"))
split=int(input("How many people to split the bill?"))
tip_c=(tip/100)*total
payment=total+tip_c
Each_pay=round((payment/split),2)
print(f"Each person should pay:{Each_pay}")
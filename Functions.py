'''In this program, we input a number, check if the number is positive or negative or zero and display an appropriate message using the functional approach and if-else statements'''

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

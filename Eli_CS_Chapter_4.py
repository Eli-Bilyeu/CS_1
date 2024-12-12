# Question 1:
number1 = int(input("First number:"))
number2 = int(input("Second number:"))
number3 = int(input("Third number:"))

smallestnumber = min(number1, number2, number3)

print("This is the smallest number:", smallestnumber)

# Question 2:
number1 = int(input("Your first number:"))
number2 = int(input("Your second number:"))

if number1 > number2:
    print(f"The bigger number between {number1} and {number2} is {number1}")

elif number2 < number1:
    print(f"The bigger number between {number1} and {number2} is {number2}")

else: 
    print(f"{number1} and {number2} have the same value")

# Question 3:

number = int(input("What number would you like to check?:"))

digits = len(str(number))

print(f"{digits} digit{'s' if digits > 1 else ''}")

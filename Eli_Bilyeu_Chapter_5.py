word = input("Make a stronger password:")
password = ''

for char in word:
    if char == 'i':
        password += '1'
    elif char == 'a':
        password += '@'
    elif char == 'm':
        password += 'M'
    elif char == 'B':
        password += '8'
    elif char == 's':
        password += '$'
    else:
    
        password += char

password += '!'

print(password)


# Question 2
loan_amount = float(input())
payment_amount = float(input())
interest_rate = float(input())

current_balance = loan_amount
payments = 0

while current_balance > 0:
    # Add interest to current balance
    current_balance += current_balance * interest_rate
    
    # Apply payment
    current_balance -= payment_amount
    
    # Increment payment counter
    payments += 1

if payments == 1:
    print(f"{payments} payment")
else:
    print(f"{payments} payments")

# Question 3
# Input the integer in the range 11-99
number = int(input())

# Check if the input is within the valid range
if number < 11 or number > 99:
    print("Input must be 11-99")
else:
    # Countdown loop
    while True:
        # Check if the digits of the number are identical
        tens = number // 10
        ones = number % 10
        if tens == ones:
            print(number)
            break
        else:
            print(number)
            number -= 1

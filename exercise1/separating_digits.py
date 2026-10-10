#separating digits of 5 digit number'
number = int(input("Enter a 5 digit number: "))
if 10000 <= number <= 99999:
    digit1 = number // 10000     # separating the first digit
    digit2 = (number // 1000) % 10  # I used the modulus operator to get the second digit and I used the floor division operator to get the first digit
    digit3 = (number // 100) % 10
    digit4 = (number // 10) % 10
    digit5 = number % 10

    print(f"The digits of the number {number} are: {digit1}, {digit2}, {digit3}, {digit4}, {digit5}")
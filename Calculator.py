num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opr = input("Enter Operations (+, -, *, /): ")

if opr == "+":
    print("Result:", num1 + num2)

elif opr == "-":
    print("Result:", num1 - num2)

elif opr == "*":
    print("Result:", num1 * num2)

elif opr == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid Operation entered")
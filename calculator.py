a = float(input("First Number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second Number: "))

if op == "+":
    print("Result:", a + b)

elif op == "-":
    print("Result:", a - b)

elif op == "*":
    print("Result:", a * b)

elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid operator.")

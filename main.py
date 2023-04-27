import calculator

print("Welcome to the magical calculator! The only operations I can abide are (+,-,*,/)")

while True:
    while True:
        try:
            num1 = float(input("Please enter the first number: "))
            break
        except ValueError:
            print("Hey bro numbers only!")

    while True:
        try:
            num2 = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("*Baffled. Try reading the prompt slower this time...")

    while True:
        operator = input("Now please select an operator (+, -, *, /) : ")

        if operator == "+":
            break
        elif operator == "-":
            break
        elif operator == "*":
            break
        elif operator == "/":
            break
        else:
            print("...sigh...")

    result = None

    while True:
        if operator == "+":
            result = calculator.add(num1, num2)
            break
        elif operator == "-":
            result = calculator.subtract(num1, num2)
            break
        elif operator == "*":
            result = calculator.multiply(num1, num2)
            break
        elif operator == "/":
            result = calculator.divide(num1, num2)
            break

    print(f"{num1} {operator} {num2} = {result}")

    use_again = input("Unfortunately I have to ask you, "
                      "but do you wanna calculate anything else? (yes/no): ").lower()

    if use_again == "yes":
        print("Ooooookk!")
        continue
    elif use_again == "no":
        print("Goodbye. Hopefully for good.")
        break
    else:
        print("Unfortunately for me, my policy says it has to be a firm no. Here we go again...")


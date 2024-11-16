def simple_calculator(num1, num2, operation):
    if operation == "mimateba":
        return num1 + num2
    elif operation == "gamokleba":
        return num1 - num2
    elif operation == "gamravleba":
        return num1 * num2
    elif operation == "gayofa":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"

while True:
    print("Choose the operation you want to perform:")
    print("1 - gayofa")
    print("2 -gamravleba")
    print("3 - mimateba")
    print("4 - gamokleba")
    print("Type 'exit' to quit the program")

    choice = input("Enter the operation number (1/2/3/4): ")
    
    if choice == 'exit':
        print("Exiting the program.")
        break

    if choice == '1':
        operation = "gayofa"
    elif choice == '2':
        operation = "gamravleba"
    elif choice == '3':
        operation = "mimateba"
    elif choice == '4':
        operation = "gayofa"
    else:
        print("Invalid choice")
        continue

    try:
        num1 = int(input('Enter your preferred first number: '))
        num2 = int(input('Enter your preferred second number: '))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    result = simple_calculator(num1, num2, operation)
    print(f"Result: {result}")

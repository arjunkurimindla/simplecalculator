def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b


def cal():
    try:
        print("\n--- Simple Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice {1-5} : ")

        if choice == '5':
            print("Thank you for using the calculator!!")

        elif choice in ['1', '2', '3', '4']:
            a = float(input("Enter first number :"))
            b = float(input("Enter first number :"))

            if choice == '1':
                print("Result:", add(a, b))
            elif choice == '2':
                print("Result:", sub(a, b))
            elif choice == '3':
                print("Result:", mul(a, b))
            elif choice == '4':
                print("Result:", div(a, b))
        else:
            print("Invalid choice! Please try again.")

        again = input("Want to use again {y/n} :").lower()
        if again == "y":
            cal()
    except ValueError:
        print("enter valid numbers only")
        cal()


cal()

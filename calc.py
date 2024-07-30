import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Function to find square root of a number
def square_root(x):
    if x < 0:
        return "Square root of negative number is not real"
    return math.sqrt(x)

# Function to find square of a number
def square(x):
    return x ** 2

# Function to calculate sine of a number
def sine(x):
    return math.sin(x)

# Function to calculate cosine of a number
def cosine(x):
    return math.cos(x)

# Function to calculate tangent of a number
def tangent(x):
    return math.tan(x)

# Function to calculate inverse sine of a number
def arcsine(x):
    if x < -1 or x > 1:
        return "Invalid input for arcsine function (input should be between -1 and 1)"
    return math.asin(x)

# Function to calculate inverse cosine of a number
def arccosine(x):
    if x < -1 or x > 1:
        return "Invalid input for arccosine function (input should be between -1 and 1)"
    return math.acos(x)

# Function to calculate inverse tangent of a number
def arctangent(x):
    return math.atan(x)

# Main function
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Square")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Inverse Sine (asin)")
    print("11. Inverse Cosine (acos)")
    print("12. Inverse Tangent (atan)")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        num = float(input("Enter a number: "))
        print("Square root of", num, "is", square_root(num))
    elif choice == '6':
        num = float(input("Enter a number: "))
        print("Square of", num, "is", square(num))
    elif choice == '7':
        num = float(input("Enter a number (in radians): "))
        print("Sine of", num, "is", sine(num))
    elif choice == '8':
        num = float(input("Enter a number (in radians): "))
        print("Cosine of", num, "is", cosine(num))
    elif choice == '9':
        num = float(input("Enter a number (in radians): "))
        print("Tangent of", num, "is", tangent(num))
    elif choice == '10':
        num = float(input("Enter a number (-1 to 1): "))
        print("Inverse Sine of", num, "is", arcsine(num))
    elif choice == '11':
        num = float(input("Enter a number (-1 to 1): "))
        print("Inverse Cosine of", num, "is", arccosine(num))
    elif choice == '12':
        num = float(input("Enter a number: "))
        print("Inverse Tangent of", num, "is", arctangent(num))
    else:
        print("Invalid input")

# Execute the main function
if __name__ == "__main__":
    main()

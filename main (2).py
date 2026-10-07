num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")

def add_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num1, num2):
    return num1 - num2
def multiply_numbers(num1, num2):
    return num1 * num2
def divide_numbers(num1, num2):
    return num1/num2

if num2 == 0:
    print("Cannot divide by zero.")
if choice == '+':
    result = add_numbers(num1, num2)
elif choice == '-':
    result = subtract_numbers(num1, num2)
elif choice == '*':
    result = multiply_numbers(num1, num2)
elif choice == '/':
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
         result = divide_numbers(num1, num2)
    
print(result)
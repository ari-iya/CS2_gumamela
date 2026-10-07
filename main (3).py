num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
choice = input("Enter operation (+, -, *, /): ")

if num2 == 0:
    print("Cannot divide by zero.")
if choice == '+':
    result = num1 + num2
elif choice == '-':
    result = num1 - num2
elif choice == '*':
    result = num1 * num2
elif choice == '/':
    result = num1/num2
    if num2 == 0:
        print("Cannot divide by zero.")
else:
    result = "Invalid/Undefined"
    
print(result)
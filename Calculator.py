#Practice creating Python programs to perform arithmetic and string, experimenting with variables, and exploring data types.
num1=3
num2=4

#operation (*, /, +, -)
operation = input

#perform the operation on numbers


if operation =='*':
    results=num1*num2
    print(f"{num1} * {num2} = {results:float}")

elif operation=='/':
    results=num1/num2
    print(f"{num1} / {num2} = {results:float}")

elif operation=='+':
    results=num1/num2
    print(f"{num1} + {num2} = {results:float}")
    
if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
        print("Error: Division by zero is not allowed.")
        print("Invalid operation entered. Please use *, /, *, and /.")


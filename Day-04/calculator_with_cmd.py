import sys
def add(num1, num2): # <function> <function Name>
    a = num1 + num2
    return a
def sub(num1, num2):
    s = num1 - num2
    return s
def mul(num1, num2):
    m = num1 * num2
    return m
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)

# python3 calculator_with_cmd.py 2 add 3

if operation == "sub":
    output = sub(num1, num2)
    print(output)

if operation == "mul":
    output = mul(num1, num2)
    print(output)

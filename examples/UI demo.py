value = input('''Welcome to the menu. Options:,
              \t 1. Roll
              \t 2. Sweep
              \t 3. Scroll
              Type number then Enter.''')
              


def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val

while True:
    if value.isdigit == True:
        value = int(value)
        break
    else:
        value=input("invalid input, please provide an integer:")

if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))

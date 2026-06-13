import sys
var = input("Enter some input: ")
print(f"Input taken with input() is always of a type {type(var)}")
while True:
    try:
        num_input = input("Enter some integer: ")
        num = int(num_input)
        print(f"You entered {num_input}.\n{num_input} + 5 = {str(num + 5)}")
        break
    except Exception:
        print("You didn't enter an integer. Try again!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by Zero.")

print("Program continues.")

try:
    number = int("Not a number")
    # number = 5 + "Not a number"
except ValueError:
    print("Error: Invalid value.")
except TypeError:
    print("Error: Invalid type.")



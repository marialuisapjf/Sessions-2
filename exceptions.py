
age = int(input("What is your age?"))
age = input("How old are you?")
age = int(age)
print(f"Your age is {age}")

try:
    age = int(input("What is your age?"))
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    print("Your age is", age)


try:
    age1 = int(input("What is your age player 1?"))
    age2 = int(input("What is your age player 2?"))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but you cannot divide by zero")
else:
    print("Player 1 is older than player 2 by a factor of", res)



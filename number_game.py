import random
x = random.randint(1,1000)
guess = None
while guess != x:
    guess = input("What is the secret Number?")
    if guess > x:
        print("Lower")
    elif guess < x:
        print("Higher")
    else:
        print("You Win!")


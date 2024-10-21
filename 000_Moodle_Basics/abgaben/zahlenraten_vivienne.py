import random
Zahl = random.randint(1, 100)


while True:
    a = int(input("enter a number."))
    if a > Zahl:
        print("the number you are looking for is smaller.")
    else:
        print("the number you are looking for is bigger.")
    if a == Zahl:
        print("You found the number")
        break
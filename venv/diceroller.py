import random, sys, os


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


runAgain = "Y"
while runAgain == "Y":
    clearScreen()
    diceNumber = int(input("How many dice would you like to roll? "))
    diceType = input("Which die would you like to roll? ")
    diceType = diceType.lower()

    while diceType == '':
        diceType = input("Please input the type of die you would like to roll: ")

    while diceNumber > 0:

        if diceType == "d2":
            print(random.randint(1, 2))
            diceNumber -= 1

        if diceType == "coin":
            coinResult = random.randint(1, 2)
            if coinResult == 1:
                print("Heads")
            else:
                print("Tails")
            diceNumber -= 1

        if diceType == "d4":
            print(random.randint(0, 4))
            diceNumber -= 1

        if diceType == 'd6':
            print(random.randint(0, 6))
            diceNumber -= 1

        if diceType == 'd8':
            print(random.randint(0, 8))
            diceNumber -= 1

        if diceType == 'd10':
            print(random.randint(0, 10))
            diceNumber -= 1

        if diceType == 'd12':
            print(random.randint(0, 12))
            diceNumber -= 1

        if diceType == 'd20':
            print(random.randint(0, 20))
            diceNumber -=1

        if diceType == 'd100':
            print(random.randint(0, 100))
            diceNumber -= 1

    if diceNumber == 0:
        runAgain = input("Would you like to roll again? [Y/N] ").upper()
        clearScreen()
        if runAgain == "N":
            quit()
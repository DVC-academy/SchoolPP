import random
from datetime import datetime

coins = 0
COIN_REWARD = 1

abacuses = 0
brainPowers = 0
calculators = 0
desktops = 0
electricity = 0

ABAC_YIELD = 1
ABAC_PRICE = 2

BRAIN_YIELD = 10
BRAIN_PRICE = 25

CALC_YIELD = 100
CALC_PRICE = 250

DESKTOP_YIELD = 1000
DESKTOP_PRICE = 2500


def printMenuAndRiddle():
    a = random.randrange(0, 10, 1)
    b = random.randrange(0, 10, 1)
    print(f''' 
    You have {coins} coins!
    Solve this for {COIN_REWARD} Coin: {a} x {b} = ? 
    Type your answer or you can type one letter to do the following actions: 
    a - Buy Abacus ({ABAC_YIELD} Coins/sec) for {ABAC_PRICE} Coin 
    b - Buy Brain ({BRAIN_YIELD} Coins/sec) power for {BRAIN_PRICE} Coin
    c - Buy Calculator ({CALC_YIELD} Coins/sec) for {CALC_PRICE} Coin
    d - Buy Desktop ({DESKTOP_YIELD} Coins/sec) computer for {DESKTOP_PRICE} Coin
    e - Buy 1 unit of Eternal happiness (it is very good) for 100 000 Coin
    p - Check inventory
    q - Quit''')
    return a * b


def stats():
    print(f''' 
    You have the followings: 
    {coins} Coin
    
    {abacuses} Abacus which makes {abacuses * ABAC_YIELD} Coins/sec 
    {brainPowers} Brain power which makes {brainPowers * BRAIN_YIELD} Coins/sec
    {calculators} Calculator which makes {calculators * CALC_YIELD} Coins/sec 
    {desktops} Desktop which makes {desktops * DESKTOP_YIELD} Coins/sec 
    {electricity} unit of Eternal happiness which is very good 
    
    In total you are making {abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD} Coins/sec ''')


userInput = 1

while userInput != 'q':
    result = printMenuAndRiddle()

    time1 = datetime.now()
    userInput = input()
    time2 = datetime.now()

    timeDiff = (time2 - time1).seconds
    coins += timeDiff * (
                abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD)
    if userInput.isnumeric():
        if int(userInput) == result:
            print(f"Great! Your reward is {COIN_REWARD} coin!")
            coins += 1
        else:
            print(f"Wrong answer! It was actually {result}, You don't get any coin :/")
        print(f"Total coins: {coins}")
    else:
        match userInput:
            case "a":
                if coins >= ABAC_PRICE:
                    coins -= ABAC_PRICE
                    abacuses += 1
                    print(f"1 Abacus added! Now you are making {abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD} Coins/sec")
                else:
                    print("You don't have enough coins to buy this :/")
            case "b":
                if coins >= BRAIN_PRICE:
                    coins -= BRAIN_PRICE
                    brainPowers += 1
                    print(f"1 Brain power added! Now you are making {abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD} Coins/sec")
                else:
                    print("You don't have enough coins to buy this :/")
            case "c":
                if coins >= CALC_PRICE:
                    coins -= CALC_PRICE
                    calculators += 1
                    print(f"1 Calculator added! Now you are making {abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD} Coins/sec")
                else:
                    print("You don't have enough coins to buy this :/")
            case "d":
                if coins >= DESKTOP_PRICE:
                    coins -= DESKTOP_PRICE
                    desktops += 1
                    print(f"1 Desktop computer added! Now you are making {abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD} Coins/sec")
                else:
                    print("You don't have enough coins to buy this :/")
            case "e":
                if coins >= 100000:
                    coins -= 100000
                    electricity += 1
                    print(f"1 unit of Eternal happiness added! That feels very good!")
                else:
                    print("You don't have enough coins to buy this :/")
            case "p":
                stats()
            case "q":
                print("Exiting the application...")
            case _:
                print(f"{userInput} is not a valid menu point. Choose a valid option!")

print("Good bye!")

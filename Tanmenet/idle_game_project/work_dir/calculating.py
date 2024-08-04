import random
from datetime import datetime
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


coins = 0
COIN_REWARD = 1

abacuses = 0
brainPowers = 0
calculators = 0
desktops = 0
happiness = 0

HAPPINESS_PRICE = 100000

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
----------------------------------------------------------------------------------
    You have {coins} coins! 
    You are making {abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD} Coins/sec
    Menu options: 
    a - Buy Abacus ({ABAC_YIELD} Coins/sec) for {real_price(ABAC_PRICE, abacuses)} Coin 
    b - Buy Brain ({BRAIN_YIELD} Coins/sec) power for {real_price(BRAIN_PRICE, brainPowers)} Coin
    c - Buy Calculator ({CALC_YIELD} Coins/sec) for {real_price(CALC_PRICE, calculators)} Coin
    d - Buy Desktop ({DESKTOP_YIELD} Coins/sec) computer for {real_price(DESKTOP_PRICE, desktops)} Coin
    e - Buy 1 unit of Eternal happiness (it is very good) for {real_price(HAPPINESS_PRICE, happiness)} Coin
    i - Check inventory
    q - Quit
Solve this for {COIN_REWARD} Coin: {a} x {b} = ?''')
    return a * b


def stats():
    print(f''' 
    You have the followings: 
    {coins} Coin
    
    {abacuses} Abacus which makes {abacuses * ABAC_YIELD} Coins/sec 
    {brainPowers} Brain power which makes {brainPowers * BRAIN_YIELD} Coins/sec
    {calculators} Calculator which makes {calculators * CALC_YIELD} Coins/sec 
    {desktops} Desktop which makes {desktops * DESKTOP_YIELD} Coins/sec 
    {happiness} unit of Eternal happiness which is very good 
    
    In total you are making {abacuses * ABAC_YIELD + brainPowers * BRAIN_YIELD + calculators * CALC_YIELD + desktops * DESKTOP_YIELD} Coins/sec ''')


def real_price(basePrice, itemCount):
    return round((1 + itemCount) * basePrice * 1.1)


def buy_item(itemName, itemVar, price, coinsVar):
    realPrice = real_price(price, itemVar)
    if coinsVar >= realPrice:
        coinsVar -= realPrice
        itemVar += 1
        print(f"1 {itemName} added!")
    else:
        print("You don't have enough coins to buy this :/")
    return itemVar, coinsVar


userInput = 1

while userInput != 'q':
    result = printMenuAndRiddle()

    time1 = datetime.now()
    userInput = input("Type your answer or choose a menu point: ")
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
    else:
        match userInput:
            case "a":
                abacuses, coins = buy_item("Abacus", abacuses, ABAC_PRICE, coins)
            case "b":
                brainPowers, coins = buy_item("Brain power", brainPowers, BRAIN_PRICE, coins)
            case "c":
                calculators, coins = buy_item("Calculator", calculators, CALC_PRICE, coins)
            case "d":
                desktops, coins = buy_item("Desktop computer", desktops, DESKTOP_PRICE, coins)
            case "e":
                happiness, coins = buy_item("unit of Eternal happiness", happiness, HAPPINESS_PRICE, coins)
            case "i":
                stats()
            case "q":
                print("Exiting the application...")
            case _:
                print(f"{userInput} is not a valid menu point. Choose a valid option!")

print("Good bye!")

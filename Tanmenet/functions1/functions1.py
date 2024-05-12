from Tanmenet.constants import INDENT
import datetime
import time

#######################################################
print(INDENT)
print("1. feladat")
# Mennyi idő telt el? Hogyan használjuk az időt? import bevezetése

start_time = datetime.datetime.now()
print(f"Starting time is: {start_time}")
# time.sleep(5)
end_time = datetime.datetime.now()
print(f"End time is: {end_time}")

print(f"Eltelt idő: {end_time - start_time}")

#######################################################


print(INDENT)
print("2. feladat")

def get_time_difference():
    start_time = datetime.datetime.now()
    print(f"Starting time is: {start_time}")
    time.sleep(5)
    end_time = datetime.datetime.now()
    print(f"End time is: {end_time}")

    print(f"Eltelt idő: {end_time - start_time}")

# get_time_difference()
# get_time_difference()

#######################################################


print(INDENT)
print("3. feladat")

number = 5
def print_number():
    number = 2
    print(number)

def print_global_number():
    global number
    print(number)






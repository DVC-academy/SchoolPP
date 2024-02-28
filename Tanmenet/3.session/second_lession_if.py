"""
# Task00 - Name guess:

-Get the user's Name as input.
-Use an if statement to determine if they are named David or not.
-Print informative messages based on this.
"""

def Task00():
    print("\n# Name guess")
    name = input("Enter your name: ")

    if name == "David":
        print("You are David!")
    else:
        print(f"You are not David :/")


"""
# Task01 - Age Eligibility:

-Get the user's age as input.
-Use an if statement to determine if they are eligible to vote.
-Print informative messages based on their age.
"""

def Task01():
    print("\n# Age Eligibility")
    voting_age = 18
    age = int(input("Enter your age: "))

    if age >= voting_age:
        print("You are eligible to vote!")
    else:
        print(f"You are not yet eligible to vote. You can vote in {voting_age - age} years.")

"""
# Task02 - Number Comparison:

-Ask the user to enter two numbers.
-Use an if statement to check if the first number is greater than, less than, or equal to the second number.
-Print appropriate messages based on the comparison.
"""

def Task02():
    print("\n# Number Comparison")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is less than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")

"""
# Task03 - Temperature Checker:

- Receive the current temperature from the user.
- Use if statements to categorize the temperature as "cold", "warm", or "hot" based on appropriate thresholds.
- Print descriptive messages based on the temperature category.
"""

def Task03():
    print("\n# Temperature Checker")
    temperature = float(input("Enter the current temperature (in °C): "))

    if temperature <= 10:
        category = "cold"
    elif temperature <= 25:
        category = "warm"
    else:
        category = "hot"

    print(f"The current temperature is {temperature}°C, which is considered {category}.")


"""
# Task04 - Grade Converter:

-Get the user's numerical grade.
-Use if statements to assign letter grades based on a grading scale (adjust ranges as needed).
-Print the letter grade equivalent.
"""

def Task04():
    print("\n# Grade Converter")
    grade = int(input("Enter your numerical grade (0-100): "))

    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"Your letter grade is: {letter_grade}")


# Comment out the functions which you don't want to run!
Task00()
Task01()
Task02()
Task03()
Task04()
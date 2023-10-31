# Chinese Zodiac Calculator-v2

from art import zodiac_art
from zodiac_dictionary import zodiac


def chinese_zodiac(year):
    for sign in range(12):
        if year % 12 == sign:
            symbol = zodiac[sign]["Animal"]
            print(zodiac_art[sign])
            element = zodiac[sign]["Element"]
            print(f"Your Chinese Zodiac Sign: {symbol}")
            print(f"Your Associated Element: {element}")

            traits = zodiac[sign]["Traits"]
            print("And your are: ")
            for i in traits:
                print(" * " + i)


print("Welcome to Chinese Zodiac Calculator!")
birth_year = int(input("Enter your birth year to know your Chinese Zodiac Sign: "))

chinese_zodiac(birth_year)

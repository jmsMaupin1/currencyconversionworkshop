import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("APIKEY")


def getCurrentConversionRates():
    res = requests.get(f"http://api.currencylayer.com/live?access_key={api_key}&format=1")
    return json.loads(res.text)["quotes"]


def getSpecificConversionRate(quotes, currency):
    return quotes[f"USD{currency}"]


def main():
    quotes = getCurrentConversionRates()
    currency = ""

    while True:
        currency = input("What currency would you like to convert from USD: ")
        currency = currency.upper()

        if currency == "EXIT":
            break

        while f"USD{currency}" not in quotes:
            currency = input("Invalid choice, please try again: ")
            currency = currency.upper()

            if currency == "EXIT":
                return

        print(getSpecificConversionRate(quotes, currency))


if __name__ == "__main__":
    main()

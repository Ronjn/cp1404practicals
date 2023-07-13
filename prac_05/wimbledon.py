"""
Emails
Estimate: 70 minutes
Actual:   45 minutes
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    champions = []
    champion_to_wins = {}
    countries = []

    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(in_file, delimiter=',')

        retrieve_champions_and_wins(champion_to_wins, champions, csv_reader)

        countries = retrieve_countries(countries, csv_reader)

        print_results(champion_to_wins, countries)


def retrieve_countries(countries, csv_reader):
    """Retrieves all winning countries from csv file and stores into set"""
    for row in csv_reader:
        countries.append(row[1])        # Adds country to the list of countries
    del countries[0]                    # Deletes the first item from the list, as that will be the literal word country
    countries = sorted(set(countries))  # Sorts the list, and makes it a set to remove duplicates
    return countries


def retrieve_champions_and_wins(champion_to_wins, champions, csv_reader):
    """Retrieves champions and number of wins and stores into dictionary"""
    for row in csv_reader:
        champions.append(row[2])       # Adds champion to the list champions
    del champions[0]                   # Deletes the first item from the list, as that will be the literal word champion
    unique_champions = set(champions)  # Creates a list of unique champions

    # Assigns the number of wins to each unique champion
    for champion in unique_champions:
        champion_to_wins[champion] = champions.count(champion)


def print_results(champion_to_wins, countries):
    """Prints the results"""
    print("Wimbledon champions:")

    # Prints name and number of wins for each champion
    for key in champion_to_wins:
        name, number_of_wins = key, champion_to_wins[key]
        print(f"{name} {number_of_wins}")

    print()
    print("There are 12 countries that have won the Wimbledon:")

    # Prints each country from the countries list
    for country in countries:
        print(f"{country}, ", end="")


main()
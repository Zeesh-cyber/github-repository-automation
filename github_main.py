import requests

from github_pipeline_functions import (
    search_github,
    filter_repositories,
    save_json,
    save_csv,
    create_report
)


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_non_negative_integer(message):
    while True:
        try:
            value = int(input(message))

            if value >= 0:
                return value

            print("Please enter 0 or a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def get_report_choice():
    while True:
        print("\nChoose a report format:")
        print("1. JSON")
        print("2. CSV")
        print("3. TXT")
        print("4. All reports")

        choice = input("Enter your choice (1-4): ")

        if choice in ["1", "2", "3", "4"]:
            return choice

        print("Please enter a number between 1 and 4.")


query = input("What do you want to search for on GitHub? ")

number = get_positive_integer(
    "How many repositories do you want? "
)

minimum_stars = get_non_negative_integer(
    "Minimum number of stars? "
)


print("\nSearching GitHub...")

repositories = search_github(query, number)

print(f"Found {len(repositories)} repositories.")

print("Filtering repositories...")

filtered_repositories = filter_repositories(
    repositories,
    minimum_stars
)

print(
    f"{len(filtered_repositories)} repositories matched your criteria."
)
choice = get_report_choice()


if choice == "1":
    print("Saving JSON...")
    save_json(filtered_repositories)

elif choice == "2":
    print("Saving CSV...")
    save_csv(filtered_repositories)

elif choice == "3":
    print("Creating report...")
    create_report(filtered_repositories)

elif choice == "4":
    print("Saving JSON...")
    save_json(filtered_repositories)

    print("Saving CSV...")
    save_csv(filtered_repositories)

    print("Creating report...")
    create_report(filtered_repositories)


print("\nPipeline completed successfully!")
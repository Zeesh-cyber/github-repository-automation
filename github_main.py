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


def get_language():
    while True:
        language = input(
            "Programming language (optional, press Enter to skip): "
        ).strip()

        if language == "":
            return None

        if language.replace("-", "").replace("_", "").isalnum():
            return language

        print("Please enter a valid programming language.")


def get_sort_choice():
    while True:
        print("\nChoose how to sort repositories:")
        print("1. Stars")
        print("2. Forks")
        print("3. Recently Updated")

        choice = input("Enter your choice (1-3): ")

        sort_options = {
            "1": "stars",
            "2": "forks",
            "3": "updated"
        }

        if choice in sort_options:
            return sort_options[choice]

        print("Please enter a number between 1 and 3.")


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


query = input(
    "What do you want to search for on GitHub? "
).strip()

number = get_positive_integer(
    "How many repositories do you want? "
)

minimum_stars = get_non_negative_integer(
    "Minimum number of stars? "
)

language = get_language()

sort_by = get_sort_choice()

print("\nSearching GitHub...")

repositories = search_github(
    query,
    number,
    language,
    sort_by,
    minimum_stars
)

print(
    f"Found {len(repositories)} repositories."
)

print("Filtering repositories...")

filtered_repositories = filter_repositories(
    repositories,
    minimum_stars
)

print(
    f"{len(filtered_repositories)} "
    "repositories matched your criteria."
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
import requests
import json
import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def search_github(query, number):
    url = "https://api.github.com/search/repositories"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code == 403:
            print("GitHub API rate limit reached.")
            return []

        response.raise_for_status()

        data = response.json()

        return data["items"][:number]

    except requests.exceptions.RequestException:
        print("Could not connect to GitHub.")
        return []


def filter_repositories(repositories, minimum_stars):
    filtered = []

    for repo in repositories:
        if repo["stargazers_count"] >= minimum_stars:
            filtered.append(repo)

    if len(filtered) == 0:
        print("No repositories matched your criteria.")

    return filtered


def save_json(repositories):
    file_path = os.path.join(BASE_DIR, "pipeline_results.json")

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(repositories, file, indent=4)


def save_csv(repositories):
    file_path = os.path.join(BASE_DIR, "pipeline_results.csv")

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Repository",
            "Stars",
            "Language",
            "URL"
        ])

        for repo in repositories:
            writer.writerow([
                repo["full_name"],
                repo["stargazers_count"],
                repo["language"],
                repo["html_url"]
            ])


def create_report(repositories):
    current_time = datetime.now()

    file_path = os.path.join(BASE_DIR, "pipeline_report.txt")

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("GITHUB AUTOMATION REPORT\n")
        file.write("========================\n\n")

        file.write(
            f"Generated on: "
            f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        file.write(
            f"Total repositories: {len(repositories)}\n\n"
        )

        for repo in repositories:
            file.write(
                f"Repository: {repo['full_name']}\n"
            )
            file.write(
                f"Stars: {repo['stargazers_count']}\n"
            )
            file.write(
                f"Language: {repo['language']}\n"
            )
            file.write(
                f"URL: {repo['html_url']}\n"
            )
            file.write("------------------------\n")


if __name__ == "__main__":

    query = input("What do you want to search for on GitHub? ")

    try:
        number = int(input("How many repositories do you want? "))
        minimum_stars = int(input("Minimum number of stars? "))

        if number <= 0 or minimum_stars < 0:
            print("Please enter valid numbers.")

        else:
            repositories = search_github(query, number)

            filtered_repositories = filter_repositories(
                repositories,
                minimum_stars
            )

            save_json(filtered_repositories)
            save_csv(filtered_repositories)
            create_report(filtered_repositories)

            print("\nPipeline completed successfully!")
            print("JSON: pipeline_results.json")
            print("CSV: pipeline_results.csv")
            print("Report: pipeline_report.txt")

    except ValueError:
        print("Please enter valid numbers.")

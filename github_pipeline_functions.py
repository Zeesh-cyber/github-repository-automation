import requests
import json
import csv
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def search_github(query, number, language=None):
    url = "https://api.github.com/search/repositories"

    search_query = query

    if language:
        search_query += f" language:{language}"

    params = {
        "q": search_query,
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
    file_path = os.path.join(
        BASE_DIR,
        "pipeline_results.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            repositories,
            file,
            indent=4
        )


def save_csv(repositories):
    file_path = os.path.join(
        BASE_DIR,
        "pipeline_results.csv"
    )

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

    file_path = os.path.join(
        BASE_DIR,
        "pipeline_report.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "GITHUB AUTOMATION REPORT\n"
        )
        file.write(
            "========================\n\n"
        )

        file.write(
            f"Generated on: "
            f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        file.write(
            f"Total repositories: "
            f"{len(repositories)}\n\n"
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

            file.write(
                "------------------------\n"
            )
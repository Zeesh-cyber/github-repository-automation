import sys
import os
import json
import csv

from unittest.mock import patch, Mock

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from github_pipeline_functions import (
    search_github,
    filter_repositories,
    save_json,
    save_csv,
    create_report
)


@patch("github_pipeline_functions.requests.get")
def test_search_github(mock_get):
    mock_response = Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "items": [
            {
                "full_name": "test/repository",
                "stargazers_count": 100
            },
            {
                "full_name": "test/another-repository",
                "stargazers_count": 80
            }
        ]
    }

    mock_get.return_value = mock_response

    result = search_github("python", 2)

    assert len(result) == 2
    assert result[0]["full_name"] == "test/repository"
    assert result[1]["full_name"] == "test/another-repository"

    mock_get.assert_called_once()


def test_filter_repositories():
    repositories = [
        {
            "full_name": "test/high-stars",
            "stargazers_count": 100
        },
        {
            "full_name": "test/low-stars",
            "stargazers_count": 20
        }
    ]

    result = filter_repositories(repositories, 50)

    assert len(result) == 1
    assert result[0]["full_name"] == "test/high-stars"


def test_save_json(tmp_path, monkeypatch):
    repositories = [
        {
            "full_name": "test/repository",
            "stargazers_count": 100
        }
    ]

    monkeypatch.setattr(
        "github_pipeline_functions.BASE_DIR",
        str(tmp_path)
    )

    save_json(repositories)

    file_path = tmp_path / "pipeline_results.json"

    assert file_path.exists()

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    assert data == repositories


def test_save_csv(tmp_path, monkeypatch):
    repositories = [
        {
            "full_name": "test/repository",
            "stargazers_count": 100,
            "language": "Python",
            "html_url": "https://github.com/test/repository"
        }
    ]

    monkeypatch.setattr(
        "github_pipeline_functions.BASE_DIR",
        str(tmp_path)
    )

    save_csv(repositories)

    file_path = tmp_path / "pipeline_results.csv"

    assert file_path.exists()

    with open(
        file_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        rows = list(csv.reader(file))

    assert rows[0] == [
        "Repository",
        "Stars",
        "Language",
        "URL"
    ]

    assert rows[1] == [
        "test/repository",
        "100",
        "Python",
        "https://github.com/test/repository"
    ]


def test_create_report(tmp_path, monkeypatch):
    repositories = [
        {
            "full_name": "test/repository",
            "stargazers_count": 100,
            "language": "Python",
            "html_url": "https://github.com/test/repository"
        }
    ]

    monkeypatch.setattr(
        "github_pipeline_functions.BASE_DIR",
        str(tmp_path)
    )

    create_report(repositories)

    file_path = tmp_path / "pipeline_report.txt"

    assert file_path.exists()

    content = file_path.read_text(
        encoding="utf-8"
    )

    assert "GITHUB AUTOMATION REPORT" in content
    assert "Total repositories: 1" in content
    assert "Repository: test/repository" in content
    assert "Stars: 100" in content
    assert "Language: Python" in content
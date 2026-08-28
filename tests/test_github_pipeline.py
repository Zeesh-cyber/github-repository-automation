import sys
import os
import json
import csv

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


def test_search_github_without_language(monkeypatch):
    class MockResponse:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {
                "items": [
                    {
                        "full_name": "test/repository",
                        "stargazers_count": 100
                    }
                ]
            }

    def mock_get(url, params, timeout):
        assert params["q"] == "AI automation"
        assert params["sort"] == "stars"
        assert params["order"] == "desc"
        assert timeout == 10
        return MockResponse()

    monkeypatch.setattr(
        "github_pipeline_functions.requests.get",
        mock_get
    )

    result = search_github(
        "AI automation",
        10
    )

    assert len(result) == 1
    assert result[0]["full_name"] == "test/repository"


def test_search_github_with_language(monkeypatch):
    class MockResponse:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {
                "items": [
                    {
                        "full_name": "test/python-ai",
                        "stargazers_count": 500,
                        "language": "Python"
                    }
                ]
            }

    def mock_get(url, params, timeout):
        assert params["q"] == "AI automation language:Python"
        assert params["sort"] == "stars"
        assert params["order"] == "desc"
        assert timeout == 10
        return MockResponse()

    monkeypatch.setattr(
        "github_pipeline_functions.requests.get",
        mock_get
    )

    result = search_github(
        "AI automation",
        10,
        "Python"
    )

    assert len(result) == 1
    assert result[0]["full_name"] == "test/python-ai"
    assert result[0]["language"] == "Python"


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

    result = filter_repositories(
        repositories,
        50
    )

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
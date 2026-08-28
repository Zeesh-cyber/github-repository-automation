# GitHub Repository Automation Tool

A Python-based automation tool that uses the GitHub REST API to search repositories, filter them by star count, and generate reports in multiple formats.

## Features

- Search GitHub repositories using the GitHub API
- Sort repositories by stars
- Filter repositories by minimum star count
- Validate user input
- Handle API connection errors
- Handle GitHub API rate limits
- Generate JSON output
- Generate CSV output
- Generate a human-readable TXT report
- Add a timestamp to generated reports
- Allow the user to choose the desired report format

## Technologies Used

- Python
- GitHub REST API
- Requests
- JSON
- CSV

## Project Structure

```text
github-repository-automation/
│
├── github_main.py
├── github_pipeline_functions.py
├── requirements.txt
├── .gitignore
└── README.md
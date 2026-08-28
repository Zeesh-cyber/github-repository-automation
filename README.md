# GitHub Repository Automation

A Python automation tool that searches GitHub repositories using the GitHub REST API, filters repositories based on their star count, and generates reports in JSON, CSV, and TXT formats.

## Overview

This project demonstrates how Python can be used to automate GitHub data collection and reporting.

The application accepts search criteria from the user, communicates with the GitHub REST API, filters the returned repositories, and generates structured reports automatically.

## Features

- Search GitHub repositories using keywords
- Specify the number of repositories to retrieve
- Filter repositories by minimum star count
- Validate user input
- Handle API and request errors
- Set request timeout protection
- Generate JSON reports
- Generate CSV reports
- Generate TXT reports
- Generate all report formats in one operation
- Include report generation date and time
- Keep generated report files out of Git using `.gitignore`

## Technologies Used

- Python
- GitHub REST API
- Requests
- JSON
- CSV
- Git
- GitHub

## Project Structure

```text
github-repository-automation/
│
├── github_main.py
├── github_pipeline_functions.py
├── requirements.txt
├── .gitignore
└── README.md
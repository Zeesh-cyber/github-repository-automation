# GitHub Repository Automation

[![Python Tests](https://github.com/Zeesh-cyber/github-repository-automation/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Zeesh-cyber/github-repository-automation/actions/workflows/python-tests.yml)

A Python automation tool that searches GitHub repositories using the GitHub REST API, filters repositories based on their star count, and generates reports in JSON, CSV, and TXT formats.

## Overview

This project demonstrates how Python can be used to automate GitHub data collection and reporting.

The application accepts search criteria from the user, communicates with the GitHub REST API, filters the returned repositories, and generates structured reports automatically.

## Features

- Search GitHub repositories using keywords
- Specify the number of repositories to retrieve
- Sort search results by stars
- Filter repositories by minimum star count
- Validate user input
- Handle API and request errors
- Set request timeout protection
- Generate JSON reports
- Generate CSV reports
- Generate TXT reports
- Include report generation date and time
- Keep generated report files out of Git using `.gitignore`
- Automated testing with pytest

## Technologies Used

- Python
- GitHub REST API
- Requests
- JSON
- CSV
- Pytest
- Git
- GitHub
- GitHub Actions

## Project Structure

~~~text
github-repository-automation/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── tests/
│   └── test_github_pipeline.py
│
├── github_main.py
├── github_pipeline_functions.py
├── requirements.txt
├── .gitignore
└── README.md
~~~

## Installation

Follow these steps to install and run the project on your computer.

### 1. Clone the repository

Open the [GitHub repository](https://github.com/Zeesh-cyber/github-repository-automation) or open a terminal or PowerShell window and run:

~~~bash
git clone https://github.com/Zeesh-cyber/github-repository-automation.git
~~~

### 2. Open the project directory

~~~bash
cd github-repository-automation
~~~

### 3. Create a virtual environment

~~~bash
python -m venv .venv
~~~

### 4. Activate the virtual environment

For Windows PowerShell:

~~~powershell
.\.venv\Scripts\Activate.ps1
~~~

### 5. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

## Usage

Run the main Python program:

~~~bash
python github_main.py
~~~

The program will ask for:

- GitHub search query
- Number of repositories to retrieve
- Minimum number of stars

The application then searches GitHub, filters the results, and automatically generates JSON, CSV, and TXT reports.

## Report Formats

### JSON

Structured repository data suitable for applications and further automation.

`pipeline_results.json`

### CSV

Tabular repository data suitable for spreadsheets and data analysis.

`pipeline_results.csv`

### TXT

A human-readable summary report.

`pipeline_report.txt`

The TXT report includes the date and time when the report was generated.

## Example Workflow

~~~text
Enter GitHub search query
        ↓
Search GitHub API
        ↓
Retrieve repositories
        ↓
Sort results by stars
        ↓
Filter by minimum stars
        ↓
Generate reports
        ↓
JSON / CSV / TXT
~~~

## Testing

This project uses `pytest` for automated testing.

Run the complete test suite with:

~~~bash
python -m pytest
~~~

The test suite verifies:

- Repository star filtering
- JSON file generation
- CSV file generation
- TXT report generation
- File creation and report contents

### Current Test Result

**5 passed**

## Continuous Integration

This project uses GitHub Actions to automatically run the test suite when changes are pushed to the `main` branch or when a pull request targets the `main` branch.

The workflow:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs project dependencies
4. Runs the complete pytest test suite

A successful workflow run confirms that the automated tests are passing.

## Error Handling

The application handles common problems such as:

- Invalid user input
- Empty search results
- GitHub API rate limits
- GitHub API request failures
- Network errors
- Request timeouts
- Invalid numeric values

## Skills Demonstrated

This project demonstrates practical experience with:

- Python programming
- Functions and modular programming
- REST API integration
- HTTP requests
- JSON data handling
- CSV file generation
- Text file generation
- Exception handling
- Input validation
- File handling
- Date and time handling
- Automated testing with pytest
- GitHub Actions CI
- Git version control
- GitHub repository management

## Future Improvements

Possible future improvements include:

- GitHub API authentication
- Pagination support
- Advanced repository filtering
- Logging
- Configuration files
- More extensive automated testing
- GitHub Actions CI/CD improvements
- Scheduled repository searches
- Additional report formats
- Web-based interface

## Author

**Zeesh Gul**

GitHub: [Zeesh-cyber](https://github.com/Zeesh-cyber)
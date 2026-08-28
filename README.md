# GitHub Repository Automation

[![Python Tests](https://github.com/Zeesh-cyber/github-repository-automation/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Zeesh-cyber/github-repository-automation/actions/workflows/python-tests.yml)
A Python automation tool that searches GitHub repositories using the GitHub REST API, filters and sorts repositories based on user-defined criteria, and generates downloadable reports in JSON, CSV, and TXT formats.

## 🌐 Live Demo

**Try the application:**  
https://repository-automation.streamlit.app/

The application is publicly deployed using Streamlit Community Cloud.

## 📌 Overview

This project demonstrates how Python can be used to automate GitHub repository discovery, filtering, sorting, pagination, data collection, and report generation.

The project provides both:

- A command-line Python application
- A Streamlit web interface

Users can search GitHub repositories using keywords, specify the number of repositories to retrieve, filter by programming language and minimum stars, sort results, and download generated reports.

## ✨ Features

- 🔎 Search GitHub repositories using keywords
- 🔢 Specify the number of repositories to retrieve
- ⭐ Filter repositories by minimum star count
- 💻 Filter repositories by programming language
- 📊 Sort repositories by Stars, Forks, or Recently Updated
- 📄 Support GitHub API pagination
- 🔗 Open repositories directly on GitHub
- 📋 Generate JSON reports
- 📊 Generate CSV reports
- 📄 Generate TXT reports
- 📦 Download all reports as a ZIP archive
- 🕒 Include report generation date and time
- 🛡️ Handle API rate limits and request errors
- ⏱️ Request timeout protection
- 🧪 Automated testing with pytest
- ⚙️ GitHub Actions continuous integration
- 🌐 Public Streamlit web application

## 🛠️ Technologies Used

- Python
- Streamlit
- GitHub REST API
- Requests
- JSON
- CSV
- Pytest
- Git
- GitHub
- GitHub Actions
- Streamlit Community Cloud

## 📁 Project Structure

| File / Directory | Purpose |
|---|---|
| `.github/workflows/python-tests.yml` | GitHub Actions CI workflow |
| `tests/test_github_pipeline.py` | Automated pytest test suite |
| `app.py` | Streamlit web application |
| `github_main.py` | Command-line application entry point |
| `github_pipeline_functions.py` | GitHub API, filtering, sorting, pagination, and report functions |
| `requirements.txt` | Python project dependencies |
| `.gitignore` | Excludes local and generated files from Git |
| `README.md` | Project documentation |

## 🧩 Application Architecture

```text
User Input
    ↓
Search Query • Repository Count • Minimum Stars • Programming Language • Sorting Option
    ↓
GitHub REST API
    ↓
API Pagination
    ↓
Filtering & Sorting
    ↓
Repository Results
    ↓
Streamlit Interface
    ↓
Report Generation
    ↓
JSON / CSV / TXT
    ↓
ZIP Download
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Zeesh-cyber/github-repository-automation.git
```

### 2. Open the project directory

```bash
cd github-repository-automation
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 💻 Run the Command-Line Application

Run:

```bash
python github_main.py
```

The command-line application allows the user to enter:

- GitHub search query
- Number of repositories
- Minimum stars
- Programming language
- Sorting preference
- Report format

## 🌐 Run the Streamlit Application Locally

To launch the web interface:

```bash
streamlit run app.py
```

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open that address in your browser.

## 🔎 Streamlit Web Interface

The web application provides:

- GitHub repository search
- Repository count selection
- Minimum-star filtering
- Programming-language filtering
- Repository sorting
- Repository result cards
- Direct GitHub repository links
- Report format selection
- Individual report downloads
- Combined ZIP report download

## 📊 Report Formats

### JSON

Structured repository data suitable for applications, scripts, and further automation.

Generated file:

`pipeline_results.json`

### CSV

Tabular repository data suitable for spreadsheets and data analysis.

Generated file:

`pipeline_results.csv`

### TXT

Human-readable repository summary containing repository information and report generation time.

Generated file:

`pipeline_report.txt`

### All Reports

The Streamlit application can package all three reports into a single ZIP archive.

Generated file:

`github_repository_reports.zip`

The ZIP contains:

- `pipeline_report.txt`
- `pipeline_results.csv`
- `pipeline_results.json`

## 🧪 Testing

This project uses pytest for automated testing.

Run the complete test suite:

```bash
pytest
```

The test suite verifies functionality including:

- Repository searching
- Programming-language filtering
- API pagination
- Minimum-star filtering
- JSON report generation
- CSV report generation
- TXT report generation

### Current Test Result

**7 tests passed**

## ⚙️ Continuous Integration

GitHub Actions automatically runs the test suite when changes are pushed to the `main` branch or when a pull request targets `main`.

Workflow file:

`.github/workflows/python-tests.yml`

The workflow:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Runs the pytest test suite
5. Reports the workflow status

A successful workflow run confirms that the automated tests are passing.

## 🛡️ Error Handling

The application handles common problems including:

- Empty search queries
- Invalid numeric values
- Empty search results
- GitHub API rate limits
- GitHub API request failures
- Network errors
- Request timeouts
- Invalid sorting selections

## 🔄 API Pagination

GitHub repository search results are returned through paginated API responses.

The application automatically requests additional pages when the requested repository count requires more results than a single API response can provide.

Pagination was validated with a live GitHub API search requesting more than 100 repositories.

## 📋 Example Workflow

```text
Enter Search Criteria
        ↓
Search GitHub REST API
        ↓
Retrieve Repository Data
        ↓
Apply Language Filter
        ↓
Apply Minimum-Star Filter
        ↓
Sort Results
        ↓
Handle API Pagination
        ↓
Display Repository Results
        ↓
Generate Reports
        ↓
JSON / CSV / TXT
        ↓
Optional ZIP Download
```

## 🎯 Skills Demonstrated

This project demonstrates practical experience with:

- Python programming
- Modular application design
- REST API integration
- GitHub API usage
- HTTP requests
- API pagination
- Data filtering
- Data sorting
- JSON processing
- CSV generation
- TXT report generation
- ZIP file creation
- Exception handling
- Input validation
- File handling
- Automated testing with pytest
- GitHub Actions
- Git version control
- GitHub repository management
- Streamlit application development
- Cloud application deployment
- Technical documentation

## 🔐 Repository Hygiene

Generated reports, virtual-environment files, Python cache directories, and other local development files are excluded through `.gitignore`.

The repository keeps source code, tests, configuration, documentation, and CI workflow files under version control.

## 📈 Development Milestones

- Initial GitHub repository automation
- Professional project documentation
- GitHub Actions CI workflow
- Programming-language filtering
- Repository sorting
- API pagination
- Expanded automated testing
- Seven-test pytest suite
- Live API validation
- Streamlit web interface
- Public Streamlit deployment
- Downloadable JSON, CSV, and TXT reports
- Combined ZIP report download
- Final repository presentation

## 🔮 Future Improvements

Possible future improvements include:

- GitHub API authentication for higher rate limits
- Advanced repository search filters
- Additional report formats
- Configurable application settings
- Structured logging
- Scheduled repository searches
- More extensive automated test coverage
- Additional Streamlit UI enhancements
- Advanced visualizations
- Improved responsive design

## 👨‍💻 Author

**Zeeshan Hassan**

GitHub:  
https://github.com/Zeesh-cyber

Project Repository:  
https://github.com/Zeesh-cyber/github-repository-automation

## 📜 License

This project is intended as a portfolio and demonstration project for Python automation, REST API integration, testing, GitHub Actions, and Streamlit application development.
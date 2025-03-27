# Curiosity

## Overview

Curiosity is a Python application that provides in-depth summaries of files in a GitHub repository, utilizing advanced language models for analysis.

## Features

- Fetches files from a GitHub repository, including nested directories.
- Utilizes AI-powered analysis to generate detailed summaries of file content, including code explanations and answers to specific questions.

## Requirements

- Python 3.x
- `PyGithub` library for interacting with the GitHub API.
- A valid GitHub token for authentication.
- `requests` library for handling HTTP requests.
- `ollama` for AI-powered analysis and summarization.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. Install the required packages:

   ```bash
   pip install PyGithub requests ollama
   ```

3. Set your GitHub token as an environment variable:

   ```bash
   export GITHUB_TOKEN='your_github_token'
   ```

## Usage

1. Run the application:

   ```bash
   python src/main.py
   ```

2. When prompted, enter the GitHub repository URL (e.g., `https://github.com/username/repository`).

3. Optionally, specify a question to ask about the repository content (e.g., `ask What is the purpose of the main.py file?`).

4. The application will fetch the content of the repository, analyze the files, and provide detailed summaries for each file, including answers to the specified question.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [PyGithub](https://pygithub.readthedocs.io/en/latest/) for the GitHub API integration.
- [Requests](https://docs.python-requests.org/en/master/) for handling HTTP requests.

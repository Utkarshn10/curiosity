# Curiosity

## Overview

Curiosity is a Python application that gives summaries of files in a GitHub repository.

## Features

- Fetches files from a GitHub repository.
- Analyzes file content and provides summaries.

## Requirements

- Python 3.x
- `PyGithub` library for interacting with the GitHub API.
- A valid GitHub token for authentication.
- ollama

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. Install the required packages:

   ```bash
   pip install PyGithub requests
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

3. The application will fetch the content of the repository and analyze the files, providing summaries for each file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [PyGithub](https://pygithub.readthedocs.io/en/latest/) for the GitHub API integration.
- [Requests](https://docs.python-requests.org/en/master/) for handling HTTP requests.

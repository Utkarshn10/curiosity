import os
from github import Github 
import logging
from explanations import analyze_files

github_token = os.getenv("GITHUB_TOKEN")
IGNORE_FILES = ['readme.md']

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_file_data(repo, file_path):
    """
    Fetches the content of a file from a GitHub repository.

    Args:
        repo (Github.Repository): The GitHub repository object.
        file_path (str): The path to the file within the repository.

    Returns:
        str or None: The decoded content of the file if it exists, otherwise None.
    """
    try:
        file_content = repo.get_contents(file_path)
        if file_content:
            return file_content.decoded_content.decode()
        else:
            return None
    except Exception as e:
        logger.error(f"Error fetching file: {file_path} - {e}")
        return None

def get_files(repo, path=""):
    """
    Recursively fetches files from a GitHub repository, excluding specified files.

    Args:
        repo (Github.Repository): The GitHub repository object.
        path (str, optional): The path within the repository to start fetching files from. Defaults to "".
    """
    contents = repo.get_contents(path)
    files_with_data = []
    for content in contents:
        file_name = content.name
        file_type = content.type
        if file_type == "dir":
            get_files(repo, content.path)
        else:
            if file_name.lower() not in IGNORE_FILES:
                file_data = get_file_data(repo, content.path)
                if file_data:
                    files_with_data = (file_name,file_data)
                    analyze_files(file_name, file_data)

def fetch_repo_content(url):
    """
    Fetches the content of a GitHub repository, excluding specified files.

    Args:
        url (str): The URL of the GitHub repository.
    """
    g = Github(github_token)
    repo = g.get_repo(url)
    files = get_files(repo)
    g.close()
    return files
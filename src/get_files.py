import os
from github import Github 
import logging
from explanations import analyze_files
from utils import extract_repo_and_file_path

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
        raise Exception(f"Error fetching file: {file_path}")
        return None

def get_files(repo, path="", question=""):
    """
    Recursively fetches files from a GitHub repository, excluding specified files.

    Args:
        repo (Github.Repository): The GitHub repository object.
        path (str, optional): The path within the repository to start fetching files from. Defaults to "".
        question (str, optional): The question to analyze the files against. Defaults to "".
    """
    try:
        contents = repo.get_contents(path)
        for content in contents:
            file_name = content.name
            file_type = content.type
            if file_type == "dir":
                get_files(repo, content.path, question)
            else:
                if file_name.lower() not in IGNORE_FILES:
                    file_data = get_file_data(repo, content.path)
                    if file_data:
                        analyze_files(file_name, file_data, question)
    except Exception as e:
        raise Exception(f"Could not get data for path: {path}")

def fetch_repo_content(url, question):
    """
    Fetches the content of a GitHub repository, excluding specified files.

    Args:
        url (str): The URL of the GitHub repository.
        question (str): The question to analyze the files against.

    Returns:
        list: A list of tuples containing the file name and its content.
    """
    try:
        g = Github(github_token)
        repo_name, file_path = extract_repo_and_file_path(url)
        repo = g.get_repo(repo_name)
        if file_path:
            file_data = get_file_data(repo, file_path)
            if file_data:
                analyze_files("", file_data, question)
        else:
            get_files(repo, question=question)
        g.close()
    except Exception as e:
        raise Exception(f"Error fetching repository content: {url}--{e}")
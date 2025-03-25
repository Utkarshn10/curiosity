"""
Main entry point for the application.
"""
import os
from github import Github 
github_token = os.getenv("GITHUB_TOKEN")

def get_file_data(repo,file_path):
    file_content = repo.get_contents(file_path)
    if file_content:
        return file_content.decoded_content.decode()
    else:
        return None

def get_files(repo):
    contents = repo.get_contents("")
    for content in contents:
        if content.type == "dir":
            get_files(repo)
        else:
            file = get_file_data(repo,content.path)
            print("file--",file)

def fetch_repo_content(url):
    g = Github(github_token)
    repo = g.get_repo(url)
    files = get_files(repo)
    g.close()


def main():
    """
    Main function that runs the application.
    """
    print("Application started")
    url = "Utkarshn10/diffy"
    fetch_repo_content(url)

if __name__ == "__main__":
    main() 
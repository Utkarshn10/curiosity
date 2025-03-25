import os
from github import Github 
import logging
from explanations import analyze_files

github_token = os.getenv("GITHUB_TOKEN")
IGNORE_FILES = ['readme.md']
cores = 2

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_file_data(repo, file_path):
    try:
        file_content = repo.get_contents(file_path)
        if file_content:
            return file_content.decoded_content.decode()
        else:
            return None
    except Exception as e:
        logger.error(f"Error fetching file: {file_path} - {e}")
        return None

def get_files(repo,path=""):
    contents = repo.get_contents(path)
    files_with_data = []
    for content in contents:
        file_name = content.name
        file_type = content.type
        if file_type == "dir":
            files_with_data.extend(get_files(repo,content.path))
        else:
            if file_name.lower() not in IGNORE_FILES:
                file_data = get_file_data(repo, content.path)
                if file_data:
                    files_with_data.append((file_name,file_data))
                    if len(files_with_data) >= cores:
                        from concurrent.futures import ThreadPoolExecutor
                        with ThreadPoolExecutor() as executor:
                            executor.map(analyze_files, [file[0] for file in files_with_data], [file[1] for file in files_with_data])
                        files_with_data = []

def fetch_repo_content(url):
    g = Github(github_token)
    repo = g.get_repo(url)
    get_files(repo)
    g.close()
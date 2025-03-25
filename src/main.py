import os
import logging
from get_files import fetch_repo_content

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    Main function that runs the application.
    """
    url = input("Enter the GitHub repository URL: ")
    if url.startswith("https://github.com/"):
        url = url.replace("https://github.com/", "")
    logger.info(f"Fetching content for repository")
    files_with_data = fetch_repo_content(url)
    
if __name__ == "__main__":
    main() 
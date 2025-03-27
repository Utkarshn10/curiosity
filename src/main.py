import os
import logging
from get_files import fetch_repo_content

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

stored_url = None
stored_question = None

def welcome_note():
    print("""
    WELCOME TO CURIOSITY

    COMMANDS:
    - `url <github_url>`: Set a GitHub repo URL (e.g., `url https://github.com/user/repo`)
    - `ask <question>`: Ask about the current repo (e.g., `ask Explain the main.py file`)
    - `exit`: Quit the program
    """)


def main():
    """
    Main function that runs the application.
    """
    welcome_note()
    global stored_url, stored_question

    while True:
        user_input =  input("\n>>> ").strip().lower()
        if user_input.startswith('url '):
            stored_url = user_input.replace("url ", "").strip()
        elif user_input.startswith('ask '):
            if not stored_url:
                print(">>>>>> Please set a GitHub URL first!")
                continue
            stored_question = user_input.replace("ask","").strip()
            stored_url = stored_url.replace("https://github.com/", "")
            logger.info(f"Fetching content for {stored_url}")
            fetch_repo_content(stored_url, stored_question)
        elif user_input.startswith("exit"):
            break
    
if __name__ == "__main__":
    main() 
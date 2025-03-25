"""
Main entry point for the application.
"""
import os
from get_files import fetch_repo_content
from explanations import analyze_files

def main():
    """
    Main function that runs the application.
    """
    print("Application started")
    url = "dhruvmanila/pie"
    files_with_data = fetch_repo_content(url)
    analyze_files(files_with_data)

if __name__ == "__main__":
    main() 
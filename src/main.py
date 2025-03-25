"""
Main entry point for the application.
"""
import os
from get_files import fetch_repo_content

def main():
    """
    Main function that runs the application.
    """
    print("Application started")
    url = "Utkarshn10/diffy"
    fetch_repo_content(url)
    
if __name__ == "__main__":
    main() 
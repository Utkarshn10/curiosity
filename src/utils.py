def extract_repo_and_file_path(url):
    """Extract repo owner/name and file path from URL."""
    parts = url.split("github.com/")[-1].split("/")
    repo_name = f"{parts[0]}/{parts[1]}"
    file_path = "/".join(parts[4:]) if "blob" in url else None
    return repo_name, file_path
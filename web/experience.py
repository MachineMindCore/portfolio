from typing import Generator
import toml
from config import CONTENT_PATH, gh_client, REPO_FILE

# Load list of repositories
repo_collection = toml.load(REPO_FILE)["PROJECTS"]

# Get user
gh_user = gh_client.get_user()

def get_jobs_data(language = "en") -> Generator[None, None, dict]:
    """
    Generator to get Github jobs data. Returns a dict with all data needed
    """
    repo_collection

def get_projects_data(language = "en") -> Generator[None, None, dict]:
    """
    Generator to get GitHub projects data. Returns a dict with all data needed
    """
    # Get data by repo
    gh_user = gh_client.get_user()
    for repo_name, branch in repo_collection:
        repo = gh_user.get_repo(repo_name)
        data_path = f"{CONTENT_PATH}/content_{language}.md"
        repo.get_contents(data_path, ref=branch)
        yield repo


if __name__ == "__main__":
    for repo in get_experience_data("PROJECTS"):
        print(repo.name)
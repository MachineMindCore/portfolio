from typing import Generator
import toml
from config import CONTENT_PATH, gh_client, REPO_FILE

def get_experience_data(category: str, language = "en") -> Generator[None, None, dict]:
    """
    Generator for experience data. Returns a dict with all data needed
    """
    # Load list of repositories
    repo_collection = toml.load(REPO_FILE)[category]

    # Get data by repo
    gh_user = gh_client.get_user()
    for repo_name, branch in repo_collection:
        repo = gh_user.get_repo(repo_name)
        data_path = f"{CONTENT_PATH}/content_{language}.md"
        #repo.get_contents(data_path, ref=branch)
        yield repo


if __name__ == "__main__":
    for repo in get_experience_data("PROJECTS"):
        print(repo.name)
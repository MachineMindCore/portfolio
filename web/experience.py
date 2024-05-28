from typing import Generator
from web.config import gh_client, OWNER, JOBS
from github.Repository import Repository
from flask import url_for

# Configure logging
#logging.basicConfig(filename='logs/error.log', level=logging.ERROR, 
#                    format='%(asctime)s %(levelname)s:%(message)s')


# Get user
gh_user = gh_client.get_user()

def get_jobs_data(language: str = "en") -> Generator[None, None, dict]:
    """
    Generator to get Github jobs data. Returns a dict with all data needed
    """
    for job_name in JOBS:
        job = gh_user.get_repo(job_name)
        yield job

def get_projects_data(language = "en"):
    starred_repos = gh_user.get_starred()
    owner_repos = filter(lambda repo: True if repo.full_name.split("/")[0] == OWNER else False, starred_repos)

    for repo in owner_repos:
        yield repo

def get_image_addr(repo: Repository):
    topics = repo.topics
    first_topic = topics[0] if len(topics)!=0 else "null"
    return url_for("static", filename=f"topics/{first_topic}.png")

def decode_job_name(repo: Repository):
    encoded_name = repo.name
    return encoded_name.replace("-", " ").replace("_", "(", 1).replace("_", ")", 1)
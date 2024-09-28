import requests
import json
from datetime import datetime
import os
import locale

from pathlib import Path

from icecream import ic

def sort_exp(collection: list, key: str):
    collection.sort(
        reverse = True,
        key = lambda obj: datetime.strptime(obj[key], "%b/%Y")
    )
    return collection

def fetch_jobs(username: str) -> list[dict[str, str]]:
    """
    Fetch jobs from a github repository containing the data. (Repository: jobs)
    """
    query_url = f'https://api.github.com/repos/{username}/jobs/contents/'
    response = requests.get(query_url)
    response.raise_for_status()
    content = json.loads(response.content)
    
    jobs = list()
    for descriptor in content:
        file_response = requests.get(descriptor["download_url"])

        metadata = json.loads(file_response.content)
        jobs.append(metadata)

    return sort_exp(jobs, "start_date")

def fetch_starred_repos(username: str) -> list[dict[str,str]]:
    """
    Fetch github starred repos which owner is username.
    """
    query_url = f'https://api.github.com/users/{username}/starred'
    response = requests.get(query_url)
    response.raise_for_status()
    content = response.json()
    
    starred_repos = list()
    for repo in content:
        id = repo["full_name"]
        if id.split("/")[0] == username:    
            languages_register = json.loads(requests.get(repo["languages_url"]).content)

            date_original = datetime.strptime(repo["created_at"], '%Y-%m-%dT%H:%M:%SZ')
            date_short = date_original.strftime('%b/%Y')

            metadata = dict()
            metadata["name"] = repo["name"]
            metadata["topics"] = repo["topics"]
            metadata["description"] = repo["description"]
            metadata["created_at"] = date_short
            metadata["languages"] = list(languages_register.keys())
            
            starred_repos.append(metadata)            
    
    return sort_exp(starred_repos, "created_at")

def save_data(folder_address: str | Path, *file_descriptors: tuple) -> None:
    """
    For every file descriptor (filname, content) write the file in the folder pointed.
    """
    for filename, file_content in file_descriptors:
        file_path = Path(folder_address, filename)
        with open(file_path, 'w') as json_file:
            json.dump(file_content, json_file, indent=4)
    
    return

if __name__ == "__main__":
    USERNAME = "MachineMindCore"
    DATA_ADDR = "data"

    repos = fetch_starred_repos(USERNAME)
    jobs = fetch_jobs(USERNAME)

    save_data(DATA_ADDR, ("jobs.json", jobs), ("repos.json", repos))



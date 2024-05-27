import os
from github import Auth, Github

def get_github_token():
    with open("token") as tokenFile:
        return tokenFile.read()

# Local vars
REPO_FILE = "repo.toml"

# GitHub Vars
GH_TOKEN = get_github_token()
gh_client = Github(GH_TOKEN)
OWNER = gh_client.get_user()
CONTENT_PATH = 'doc/'
BRANCH = 'main'

# Flask vars
TEMPLATE_DIR = os.path.abspath("templates/")
STATIC_DIR = os.path.abspath("styles/")
CONTENT_DIR = os.path.abspath("styles/content/")

TEMPLATES = {
    "profile": {
        "base": "profile.html"
    },

    "experience": {
        "base": "experience.html",
        "job": "job_content.html",
        "project": "project_content.html"
    },

    "contact": {
        "base": "contact.html"
    }
}


# Directories adn links
PROJECTS_URL = {
    "project_demo": "https://localhost/"
}


# Constants

LANGUAGES = {
    "Español": "es",
    "English": "en"
}


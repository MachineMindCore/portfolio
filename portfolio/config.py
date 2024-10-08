import os
from github import Github
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Local vars
REPO_FILE = "repo.toml"

# GitHub Vars
GH_TOKEN = os.getenv("GH_TOKEN")
gh_client = Github(GH_TOKEN)
OWNER = "MachineMindCore"
JOBS = ["RPA-Developer_Pidgin_"]


TEMPLATES = {
    "profile": "profile.html",
    "experience": "experience.html",
    "contact": "contact.html",
    "animation": "animation.html"
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


import os

# Templates

TEMPLATE_DIR = os.path.abspath("templates/")

STATIC_DIR = os.path.abspath("templates/styles/")

TEMPLATES = {
    "home": {
        "base": "home.html"
    },

    "projects": {
        "base": "projects.html",
        "content": "project_content.html"
    },

    "contact": {
        "base": "contact.html"
    }
}


# Directories adn links


CONTENT_DIR = "content"

PROJECTS_URL = {
    "project_demo": "https://localhost/"
}


# Constants

LANGUAGES = {
    "Español": "es",
    "English": "en"
}


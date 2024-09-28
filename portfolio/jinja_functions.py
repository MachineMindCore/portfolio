from flask import url_for
from github.Repository import Repository
from datetime import datetime

from requests import get

LOGO_TOPICS = {"package", "web", "dash", "pidgin"}

def get_logo_addr(obj: dict[str, str]) -> str:
    """
    From the main topic of the object return the matching topic image.
    """
    topics = set(obj["topics"])
    common_topics = topics.intersection(LOGO_TOPICS)
    main_topic = common_topics.pop() if len(common_topics) > 0 else "python" 
    return url_for("static", filename=f"topics/{main_topic}.png")

def get_languages(obj: dict[str, str]) -> str:
    """
    Format language list into a string.
    """
    languages_str = ""
    
    for lang in obj["languages"]:
        languages_str += f", {lang}"
    return languages_str[2:]

def get_technologies(obj: dict[str, str]) -> str:
    """
    Format language list into a string.
    """
    technologies_str = ""
    
    for lang in obj["technologies"]:
        technologies_str += f", {lang}"
    return technologies_str[2:]
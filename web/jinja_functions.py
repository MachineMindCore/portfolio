from flask import url_for
from github.Repository import Repository
from datetime import datetime

from requests import get

def get_image_addr(repo: Repository):
    topics = repo.topics
    first_topic = topics[0] if len(topics)!=0 else "null"
    return url_for("static", filename=f"topics/{first_topic}.png")

def decode_job_name(repo: Repository):
    encoded_name = repo.name
    return encoded_name.replace("-", " ").replace("_", "(", 1).replace("_", ")", 1)

def get_languages(repo: Repository):
    languages = repo.get_languages().keys()
    return ', '.join(lang for lang in languages)

def get_date(repo: Repository):
    date_raw = repo.created_at
    return date_raw.strftime("%b/%Y")
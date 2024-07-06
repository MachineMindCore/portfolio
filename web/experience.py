import json

from typing import Generator
from web.config import gh_client, OWNER, JOBS
from pathlib import Path
# Configure logging
#logging.basicConfig(filename='logs/error.log', level=logging.ERROR, 
#                    format='%(asctime)s %(levelname)s:%(message)s')


# Get user
gh_user = gh_client.get_user()

DATA_ADDR = Path.home() / "Data/portfolio/"

def get_exp_data(filename: str) -> list[dict[str, str]]:
    """
    Generator to get Github jobs data. Returns a dict with all data needed
    """
    file_path = Path(DATA_ADDR, filename)
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
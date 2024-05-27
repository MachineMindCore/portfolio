import markdown
import os
import toml
from config import CONTENT_DIR

def get_subfolders(folder_path: str):
    subfolders = []    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders.append(item_path)
    return subfolders


def extract_project_data(project_dir: str, language: str = "en") -> dict:
    """
    Extract data from projects directory and build html renderization.
    """
    # Content files
    attributes_file = f"{project_dir}/attributes_{language}.toml"
    icon_file = f"{project_dir}/icon.png"
    description_file = f"{project_dir}/description_{language}.md"

    # Content
    with open(description_file, 'r') as file:
        description_content = file.read()
        attributes_content = toml.load(attributes_file)
    
    # Build data
    description_data = {
        "long_description": ""#markdown.markdown(description_content) FURTHER IMPLEMENTATION
    }
    icon_data = {
        "icon_addr": icon_file
    }

    project_data = {**attributes_content, **description_data, **icon_data}
    return project_data


def extract_pcards_data(language: str = "en") -> list:
    # Get subfolders
    subfolder_addrs = get_subfolders(f"{CONTENT_DIR}/projects")
    
    # Collect data by project
    projects_data = list()
    for project_addr in subfolder_addrs:
        sample_data = extract_project_data(project_addr, language=language)
        projects_data.append(sample_data)
    
    return projects_data
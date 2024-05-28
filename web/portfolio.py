from web.experience import get_jobs_data, get_projects_data, get_image_addr
from web.config import TEMPLATES, TEMPLATE_DIR, STATIC_DIR
from flask import (
    Flask, request,
    render_template, redirect, url_for
)
from jinja2 import Environment

# App
portfolio = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR, static_url_path=STATIC_DIR)



# Endpoints

@portfolio.route('/')
def index():
    return redirect('/profile')

@portfolio.route('/profile')
def home():
    return render_template(TEMPLATES["profile"]["base"])

@portfolio.route('/experience', methods=['GET'])
def projects():
    jobs_data = get_jobs_data()
    projects_data = get_projects_data()
    return render_template(TEMPLATES["experience"]["base"], projects_data=projects_data, jobs_data=jobs_data)

@portfolio.route('/contact')
def contact():
    return render_template(TEMPLATES["contact"]["base"])

portfolio.jinja_env.filters['get_icon'] = get_image_addr

if __name__ == '__main__':
    portfolio.run(debug=True)

from .experience import get_exp_data
from .jinja_functions import get_logo_addr, get_languages, get_technologies
from .config import TEMPLATES, TEMPLATE_DIR, STATIC_DIR
from flask import Flask, render_template, redirect, stream_with_context, Response
from icecream import ic

# App
portfolio = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR, static_url_path=STATIC_DIR)

# Endpoints
@portfolio.route('/')
def index():
    return redirect('/profile')

@portfolio.route('/profile')
def home():
    return render_template(TEMPLATES["profile"])

@portfolio.route('/experience', methods=['GET'])
def experience():
    jobs_data = get_exp_data("jobs.json")
    projects_data = get_exp_data("repos.json")
    ic(jobs_data)
    ic(projects_data)
    return render_template(TEMPLATES["experience"], projects_data=projects_data, jobs_data=jobs_data)
    
@portfolio.route('/contact')
def contact():
    return render_template(TEMPLATES["contact"])

@portfolio.route('/animation')
def animation():
    return render_template(TEMPLATES["animation"])

portfolio.jinja_env.filters['get_icon'] = get_logo_addr
portfolio.jinja_env.filters['get_languages'] = get_languages
portfolio.jinja_env.filters['get_techs'] = get_technologies

if __name__ == '__main__':
    from waitress import serve
    serve(portfolio, host="0.0.0.0", port=8080)

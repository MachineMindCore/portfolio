from .experience import get_jobs_data, get_projects_data
from .jinja_functions import get_image_addr, get_languages, decode_job_name, get_date
from .config import TEMPLATES, TEMPLATE_DIR, STATIC_DIR
from flask import Flask, render_template, redirect, stream_with_context, Response
from flask_caching import Cache
from .timing import tic, toc

# App
portfolio = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR, static_url_path=STATIC_DIR)
cache = Cache(portfolio)


# Endpoints

@portfolio.route('/')
def index():
    return redirect('/profile')

@portfolio.route('/profile')
def home():
    return render_template(TEMPLATES["profile"])

@portfolio.route('/experience', methods=['GET'])
@cache.cached(timeout=60)
def projects():
    jobs_data = get_jobs_data()
    projects_data = get_projects_data()
    return render_template(TEMPLATES["experience"], projects_data=projects_data, jobs_data=jobs_data)
    
@portfolio.route('/contact')
def contact():
    return render_template(TEMPLATES["contact"])

@portfolio.route('/animation')
def animation():
    return render_template(TEMPLATES["animation"])

portfolio.jinja_env.filters['get_icon'] = get_image_addr
portfolio.jinja_env.filters['decode_job'] = decode_job_name
portfolio.jinja_env.filters['get_languages'] = get_languages
portfolio.jinja_env.filters['get_date'] = get_date

if __name__ == '__main__':
    from waitress import serve
    serve(portfolio, host="0.0.0.0", port=8080)

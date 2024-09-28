from portfolio.experience import get_exp_data
from portfolio.jinja_functions import get_logo_addr, get_languages, get_technologies
from portfolio.config import TEMPLATES
from flask import Flask, render_template, redirect, stream_with_context, Response, url_for

# App
portfolio = Flask(__name__)
 
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

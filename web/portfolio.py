import os
from handlers import extract_pcards_data
from config import TEMPLATES, TEMPLATE_DIR, STATIC_DIR
from flask import (
    Flask, request,
    render_template, redirect, url_for
)

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
    projects_data = extract_pcards_data()
    return render_template(TEMPLATES["experience"]["base"], projects_data=projects_data)

@portfolio.route('/contact')
def contact():
    return render_template(TEMPLATES["contact"]["base"])

if __name__ == '__main__':
    portfolio.run(debug=True)

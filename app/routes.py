from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Simon'}
    return render_template('index.html', title='Simon\'s homepage', user=user)

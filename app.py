from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyshorteners
import validators
# import win32api

app = Flask(__name__)

############# Database Configuration ###############

basedir = os.path.abspath(os.path.dirname(__file__))
path = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#####################################################

class URLShortener(db.Model):
    __tablename__ = 'sabjis'
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.Text)
    shorted_url = db.Column(db.Text)
    def __init__(self, original_url, shorted_url):
        self.original_url = original_url
        self.shorted_url = shorted_url
    def __repr__(self):
        return "Original URL - {} and Shorted URL - {}".format(self.original_url, self.shorted_url)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not validators.url(url):
            return render_template('index.html', alert=True)
        s = pyshorteners.Shortener()
        shorter = s.tinyurl.short(url)

        # save url to the databases
        url_shortener = URLShortener(original_url=url, shorted_url=shorter)
        db.session.add(url_shortener)
        db.session.commit()

        return render_template('index.html', shorter=shorter)
    return render_template('index.html')

@app.route('/history')
def history():
    urls = URLShortener.query.all()
    return render_template('history.html', urls=urls)

if __name__ =='__main__':
    app.run(debug=True)
"""Main module"""

from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash
from logging import DEBUG
from forms import BookmarkForm
# from flask_wtf.csrf import CsrfProtect

SECRET_KEY = '\xfdq\xd7\x0b\xfa\x1c\xd3\xcd\x9fZ\x7f\x15\x8a\xfb\xed\xc6\xdf\xbc-\xd5\xff\xcbfl'

APP = Flask(__name__)
APP.secret_key = SECRET_KEY
APP.config['SECRET_KEY'] = SECRET_KEY
# CsrfProtect(APP)
APP.logger.setLevel(DEBUG)

bookmarks = []


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


def store_bookmark(url):
    """
    saves bookmark
    """
    bookmarks.append(
        dict(
            url=url,
            user="dmitry",
            date=datetime.utcnow()))


class User(object):
    """
    User to save
    """

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        """
        Initials
        """
        return "{}. {}.".format(self.firstname[0], self.firstname[0])


@APP.route('/')
@APP.route('/index')
def index():
    """
    by default looks in templates folder
    """

    APP.logger.debug('In the index method')
    return render_template("index.html", new_bookmarks=new_bookmarks(5))


@APP.route('/add', methods=['GET', 'POST'])
def add():
    """
    adds urls
    """

    APP.logger.debug('In the add method')

    form = BookmarkForm()

    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url)
        flash("Stored '{}-{}'".format(url, description))
        return redirect(url_for('index'))

    if form.errors:
        APP.logger.debug('Not valid')
        APP.logger.debug(form.errors)

    return render_template('add.html', form=form)

    """Old way"""
    """if request.method == "POST":
        url = request.form['url']
        save_bookmark(url)
        return redirect(url_for('index'))
    return render_template("add.html")"""


@APP.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@APP.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500


def save_bookmark(url):
    store_bookmark(url)
    flash('Stored url: ' + url)
    APP.logger.debug('Stored url: ' + url)


if __name__ == "__main__":
    APP.run(debug=True)

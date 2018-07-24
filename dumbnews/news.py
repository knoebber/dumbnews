from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from dumbnews.auth import login_required
from dumbnews.db import get_db

from dumbnews.get_news import *
from dumbnews.sort_news import sorts

bp = Blueprint('news', __name__)

@bp.route('/')
def index():
    if not g.user:
        return redirect(url_for('auth.login'))

    titles = list_titles()

    return render_template('news/feeds.html', titles=titles)

@bp.route('/news/<title>')
@login_required
def news(title):

    path = get_path(title)
    feeds = get_feeds(path)

    return render_template('news/news.html', title=title, feeds=feeds, sorts=sorts)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from dumbnews.auth import login_required
from dumbnews.db import get_db

bp = Blueprint('news', __name__)

@bp.route('/')
@login_required
def index():
    return('Nice')

from flask import (
    Blueprint,
    Response,
    abort,
    current_app,
    jsonify,
    redirect,
    render_template,
    request,
)
from jinja2 import TemplateNotFound
import validators

from app.controller import create_tiny_url, get_url, get_url_by_longurl
from . import db

bp = Blueprint("app", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/<file>.html")
def route_file(file):
    try:
        return render_template(f"{file}.html")
    except TemplateNotFound:
        abort(404)


@bp.route("/generate", methods=["POST"])
def generate():
    longurl = request.form.get("longurl")

    if not longurl:
        return jsonify(error="Did not receive the long url")

    # validate the url
    if not validators.url(longurl):
        return jsonify(error="Invalid URL")

    # check if it exists in the database
    url = get_url_by_longurl(longurl)

    if not url:
        urlid = create_tiny_url(longurl)
    else:
        urlid = url["urlid"]

    return jsonify(url=f'{current_app.config["HOST"]}/{urlid}')


@bp.route("/<urlid>")
def redirect_tiny_url(urlid):
    url = get_url(urlid)

    if not url:
        abort(404)

    return redirect(url["url"], code=302)


@bp.errorhandler(404)
def handle_404_error(e):
    return render_template("404.html"), 404

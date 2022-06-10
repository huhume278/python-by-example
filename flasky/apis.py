from flask import Blueprint

diff_api = Blueprint("diff_api",__name__)

@diff_api.route('/get')
def get():
    return "/get"


@diff_api.route('/post')
def post():
    return "/post"
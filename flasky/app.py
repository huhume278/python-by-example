from sys import prefix
from flask import Flask

app = Flask(__name__)
from .apis import diff_api as diff_api_blueprint

app.register_blueprint(diff_api_blueprint,prefix_url="/diff")

@app.route('/get',defaults={"query":"name"})
def index(query):
    return {"body":{"query":query}}
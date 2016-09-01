from flask import Flask, redirect, url_for, request
from link_shortener import *


app = Flask(__name__)
link_shortener = LinkShortener()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return redirect(url_for('static', filename="index.html"))
    else:
        return link_shortener.get_code_url(request.form['url'])


@app.route('/link/<code>')
def link(code):
    return redirect(link_shortener.get_url(code))

if __name__ == '__main__':
    app.run(debug=True)

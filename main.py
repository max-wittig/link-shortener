from flask import Flask, redirect, url_for, request, render_template
from link_shortener import *
from urllib.parse import urlparse


app = Flask(__name__)
link_shortener = LinkShortener()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return redirect(url_for('static', filename="index.html"))
    else:
        url = urlparse(request.url)
        hostname = url.hostname
        code_url = link_shortener.get_code_url(request.form['url'], hostname)
        return render_template('short_link.html', code_url=code_url)

@app.route('/link/<code>')
def link(code):
    return redirect(link_shortener.get_url(code))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=link_shortener.port)

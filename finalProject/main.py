from flask import Flask, render_template, jsonify, json
import util


app = Flask(__name__)


@app.route('/')
def index():
    # this is your index/homepage page
    log = 'homepage.'
    return render_template('index.html', log_index = log)

@app.route('/request')
def request():
    # this is your create a request page
    log = 'request.'
    return render_template('request.html', log_request = log)

@app.route('/accept')
def accept():
    # this is your accept a request page
    log = 'accept.'
    return render_template('accept.html', log_accept = log)

@app.route('/status')
def status():
    # this is your request status page
    log = 'status.'
    return render_template('status.html', log_status = log)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)


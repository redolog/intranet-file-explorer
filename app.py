# !/usr/bin/env python3
# coding=utf8
import argparse
import os

from flask import Flask, abort, send_file, jsonify
from flask import render_template
from flask import request

app = Flask(__name__)
DEFAULT_PORT = 5000
# limit file size 500MB
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000
UPLOAD_DIR = os.path.curdir + '/upload/'


@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    abs_path = os.path.join(os.path.curdir, req_path)

    if not os.path.exists(abs_path):
        return abort(404)

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    return render_template('index.html', files=files)


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    file.save(UPLOAD_DIR + file.filename)
    return jsonify({'success': True})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port",
                        help=f"Assign a port you'd like the server bind to, the default port is {DEFAULT_PORT}",
                        type=int, default=DEFAULT_PORT)
    args = parser.parse_args()
    port = args.port
    # Start the server
    print(f"Flask server started port:{port}")
    app.run('127.0.0.1', port, debug=False)

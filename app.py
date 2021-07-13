from flask import Flask
from flask import json
from flask import request
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(filename='app.log',level=logging.DEBUG)

@app.route("/")
def hello():
    app.logger.info("%s, %s endpoint was reached", datetime.now(), request.url_rule)
    return "Hello World!"

@app.route('/status')
def status():
    app.logger.info("%s, %s endpoint was reached", datetime.now(), request.url_rule)
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route('/metrics')
def metrics():
    app.logger.info("%s, %s endpoint was reached", datetime.now(), request.url_rule)
    response = app.response_class(
            response=json.dumps({"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

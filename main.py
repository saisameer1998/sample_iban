from flask import Flask
from iban.validator import Validator

import os
import json


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['APPLICATION_ROOT'] = '/iban'


@app.route('/iban/validate/<string:iban>')
def call_validator(iban) -> str:
    """
    Function to route validate api call
    :return: String stating if the provide d IBAN is valid 
    """

    response  = {'message': Validator(iban).validate()}
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST', '0.0.0.0'), port=os.getenv('PORT', 12345))

from app.api.application_api import apiv1
import os
from app import create_app, db
from flask_migrate import Migrate
from flask_script import Manager
from app.api.sample import api as sample_ns
from app.api.utility import api as utility_ns

app = create_app(os.getenv('ENV_CONFIG') or 'default')
app.register_blueprint(apiv1)
manager = Manager(app)
migrate = Migrate(app, db)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,PATCH,POST,DELETE')
    return response

if __name__ == '__main__':
    # Running in Non-Production mode
    import logging

    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run()

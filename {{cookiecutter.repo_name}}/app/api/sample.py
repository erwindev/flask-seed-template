from app.api.application_api import api, sample_ns
from flask import jsonify
from app.service.sample_service import SampleService
from flask_restplus import Resource
from app.application_exception import ApplicationException


# Required routes
@api.route("/seed/v1/sample/")
class Sample(Resource):
    """
    This class contains the functions to run the API request.
    HTTP methods are implemented as functions.  Currently,
    this API only supports HTTP GET
    """

    @sample_ns.doc('runsample')
    def get(self):
        """Run the sample request"""
        try:
            service = SampleService()
            message = service.process()
            return jsonify(message=message)
        except ApplicationException as e:
            error_message = str(e)
            return jsonify(message=error_message[:200])

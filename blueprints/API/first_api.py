from flask import Response, request, json
from flask_restful import Resource

class FakeApi(Resource):

    # Get
    def get(self):
        return Response(response=json.dumps({
            "data": "Berhasil"
        }), mimetype="application/json", status=200)
    
    # Post
    def post(self):
        # Get Requested data (Raw)
        sent_data = request.get_json()

        return Response(response=json.dumps({
            "data": sent_data
        }), mimetype="application/json", status=200)
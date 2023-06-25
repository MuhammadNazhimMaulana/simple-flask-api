from flask import Response, request, json
from flask_restful import Resource

# Without ID
class FakesApi(Resource):

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

# With Id
class FakeApi(Resource):
    # Put one
    def put(self, id):
        body = request.get_json()

        return Response(response=json.dumps({
            "message": "Update Successful",
            "data": body,
            "id": id
        }), mimetype="application/json", status=200)
    
    # Delete One
    def delete(self, id):

        return Response(response=json.dumps({
            "message": "Delete Successful",
            "id": id
        }), mimetype="application/json", status=200)

    # Get one
    def get(self, id):
        return Response(response=json.dumps({
            "message": "Get Detail Data Successful",
            "id": id
        }), mimetype="application/json", status=200)

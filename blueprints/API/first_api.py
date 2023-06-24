from flask import Response, request, jsonify
from flask_restful import Resource

class FakeApi(Resource):
    def get(self):
        return Response("Berhasil", mimetype="application/json", status=200)
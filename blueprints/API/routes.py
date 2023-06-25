from .first_api import FakesApi, FakeApi

def initialize_routes(api):
    api.add_resource(FakesApi, '/api/fakes')
    api.add_resource(FakeApi, '/api/fakes/<id>')
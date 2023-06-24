from .first_api import FakeApi

def initialize_routes(api):
    api.add_resource(FakeApi, '/api/fakes')
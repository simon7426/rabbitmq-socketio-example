from flask_restx import Api

from project.api.alive import alive_namespace
from project.api.events import winner_namespace

api = Api(version="1.0", title="Winner announcer api", doc="/docs")

api.add_namespace(alive_namespace, path="/api/v1/winner/alive")
api.add_namespace(winner_namespace, path="/api/v1/winner/update")

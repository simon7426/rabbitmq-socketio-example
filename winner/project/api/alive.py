from flask_restx import Namespace, Resource

alive_namespace = Namespace("Alive")


@alive_namespace.route("")
class Alive(Resource):
    def get(self):
        return {"message": "alive"}

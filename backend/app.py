# from flasgger import Swagger
from data import db_session
from flask_restful import Api
from flask import Flask, redirect
from data.user_resource import UserResource, UserListResource
from data.dashboard_resource import GroupResource, GroupListResource
from data.parse_resource import ParseRequestResource
from config.config import HOST, PORT, DEBUG, DATABASE, SITE_IP
import logging

app = Flask(__name__)
api = Api(app)
# swagger = Swagger(app)
logging.basicConfig(filename='logs/logs.log', filemode='w')
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)


@app.route("/ping")
def ping():
    return {"answer": "pong!"}


db_session.global_init(DATABASE)
api.add_resource(UserResource, "/api/users/<int:user_id>")
api.add_resource(UserListResource, "/api/users")
api.add_resource(GroupResource, "/api/groups/<int:group_id>")
api.add_resource(GroupListResource, "/api/groups")
api.add_resource(ParseRequestResource, "/api/parsing")
api.init_app(app)

if __name__ == '__main__':
    if DEBUG:
        app.run(host=HOST, port=PORT, debug=DEBUG)

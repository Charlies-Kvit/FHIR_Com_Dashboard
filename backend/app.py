# from flasgger import Swagger
from data import db_session
from flask_restful import Api
from flask import Flask, redirect
from data.account_resource import AccountResource, AccountListResource
from data.group_resource import GroupResource, GroupListResource
from data.parse_resource import ParseRequestResource, ParseRequestListResource
from config.config import HOST, PORT, DEBUG, DATABASE
import logging

app = Flask(__name__)
# swagger = Swagger(app)
api = Api(app)
logging.basicConfig(filename='logs/logs.log', filemode='w')
logger = logging.getLogger('flask')
logger.setLevel(logging.DEBUG)


@app.route("/ping")
def ping():
    return {"answer": "pong!"}



db_session.global_init(DATABASE)
api.add_resource(AccountResource, "/api/accounts/<int:account_id>")
api.add_resource(AccountListResource, "/api/accounts")
api.add_resource(GroupResource, "/api/groups/<int:group_id>")
api.add_resource(GroupListResource, "/api/groups")
api.add_resource(ParseRequestResource, "/api/parsing/<account_email>")
api.add_resource(ParseRequestListResource, "/api/parsing")
api.init_app(app)

if __name__ == '__main__':
    if DEBUG:
        app.run(host=HOST, port=PORT, debug=DEBUG)

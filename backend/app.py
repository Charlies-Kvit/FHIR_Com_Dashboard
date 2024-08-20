# from flasgger import Swagger
from data import db_session
from flask_restful import Api
from flask import Flask, redirect
from data.auto_update_parse import update
from data.account_resource import AccountResource, AccountListResource
from data.group_resource import GroupResource, GroupListResource
from data.parse_resource import ParseRequestResource, ParseRequestListResource
from config.config import HOST, PORT, DEBUG, DATABASE
import logging

app = Flask(__name__)
# swagger = Swagger(app)
api = Api(app)
logging.basicConfig(filename='logs/logs.log', filemode='a')
logger = logging.getLogger('flask')
logger.setLevel(logging.DEBUG)


@app.route("/ping")
def ping():
    return {"answer": "pong!"}


@app.errorhandler(404)
def error_404(*_):
    return {"ERROR": 404}, 404


@app.errorhandler(500)
def error_500(*_):
    return {"ERROR": "500, please, give a feedback on this email: theivangao@gmail.com"}, 500


db_session.global_init(DATABASE)
app.add_url_rule("/update_parsing", "update", update)
api.add_resource(AccountResource, "/api/accounts/<int:account_id>")
api.add_resource(AccountListResource, "/api/accounts")
api.add_resource(GroupResource, "/api/groups/<int:group_id>")
api.add_resource(GroupListResource, "/api/groups")
api.add_resource(ParseRequestResource, "/api/parsing/<int:account_id>")
api.add_resource(ParseRequestListResource, "/api/parsing")
api.init_app(app)

if __name__ == '__main__':
    if DEBUG:
        app.run(host=HOST, port=PORT, debug=DEBUG)

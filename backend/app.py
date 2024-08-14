# from flasgger import Swagger
from data import db_session
from flask_restful import Api
from flask import Flask, redirect
from data.auto_update_parse import update
from data.account_resource import AccountResource, AccountListResource
from data.group_resource import GroupResource, GroupListResource
from data.parse_resource import ParseRequestResource, ParseRequestListResource
from config.config import HOST, PORT, DEBUG, DATABASE
import datetime
import time
import threading
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


@app.errorhandler(404)
def error_404(*_):
    return {"ERROR": 404}, 404


@app.errorhandler(500)
def error_500(*_):
    return {"ERROR": "500, please, give a feedback on this email: theivangao@gmail.com"}, 500


def time_checker():
    delta = datetime.timedelta(hours=3, minutes=0)
    date = (datetime.datetime.now(datetime.timezone.utc) + delta).strftime('%H:%M')
    hours = int(date[:date.find(":")])
    minutes = int(date[date.find(":") + 1:])
    if hours == 23 and 55 <= minutes <= 56:
        logger.info("Началось автообновление бд")
        update()
    time.sleep(60)





db_session.global_init(DATABASE)
app.add_url_rule("/update_parsing", "update", update)
api.add_resource(AccountResource, "/api/accounts/<int:account_id>")
api.add_resource(AccountListResource, "/api/accounts")
api.add_resource(GroupResource, "/api/groups/<int:group_id>")
api.add_resource(GroupListResource, "/api/groups")
api.add_resource(ParseRequestResource, "/api/parsing/<int:account_id>")
api.add_resource(ParseRequestListResource, "/api/parsing")
api.init_app(app)
x = threading.Thread(target=time_checker)

"""def checker_thread():
    while True:
        print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
        time.sleep(5)

if __name__ == '__main__':
    x = threading.Thread(target=checker_thread)
    x.start()

    app.run(debug=True)
"""
if __name__ == '__main__':
    if DEBUG:
        app.run(host=HOST, port=PORT, debug=DEBUG)

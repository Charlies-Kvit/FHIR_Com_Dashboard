from . import db_session
from flask_restful import abort, Resource, reqparse
from .groups import Groups
from flask import abort, jsonify

parser = reqparse.RequestParser()
parser.add_argument("group_name")


def abort_id_group_not_found(group_id):
    db_sess = db_session.create_session()
    group = db_sess.query(Groups).get(group_id)
    db_sess.close()
    if not group:
        abort(404, f"Group {group_id} not found")


class GroupResource(Resource):
    def get(self, group_id):
        abort_id_group_not_found(group_id)
        db_sess = db_session.create_session()
        group = db_sess.query(Groups).get(group_id)
        db_sess.close()
        return jsonify(
            {'group': group.to_dict(only=("id", "name"))}
        )

    def put(self, group_id):
        abort_id_group_not_found(group_id)
        args = parser.parse_args()
        db_sess = db_session.create_session()
        group = db_sess.query(Groups).get(group_id)
        group.name = args['group_name']
        db_sess.commit()
        db_sess.close()
        return {"success": "OK"}

    def delete(self, group_id):
        abort_id_group_not_found(group_id)
        db_sess = db_session.create_session()
        group = db_sess.query(Groups).get(group_id)
        
        db_sess.delete(group)
        db_sess.commit()
        db_sess.close()
        return {"success": "OK"}


class GroupListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        groups = db_sess.query(Groups).all()
        db_sess.close()
        return jsonify({
            "groups":
                [group.to_dict(only=('id', 'name')) for group in groups]
        })

    def post(self):
        db_sess = db_session.create_session()
        args = parser.parse_args()
        group = Groups(
            name=args['group_name']
        )
        db_sess.add(group)
        db_sess.commit()
        db_sess.close()
        return jsonify(
            {'group': group.to_dict(only=("id", "name"))}
        )

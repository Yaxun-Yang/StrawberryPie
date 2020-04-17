from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from ..models import Warn, Dormcondition
from App.ext import db
from App.views.first import user
warn = Blueprint('warn', __name__)


@warn.route("/api/air", methods=['GET'])
def warn_air():
    room_num = user.roomnum
    warn_student = Dormcondition.query.filter(Dormcondition.address.contains(room_num)).all()
    condition = []
    warning_condition = []
    if warn_student is not None:
        for w in warn_student:
            if w.aircondition == 1:
                condition.append("空调异常")
                warning_condition.append(True)
            else:
                condition.append("正常")
                warning_condition.append(False)
        response_consume_dic = {
            "data": {
              "airconditon": condition[0],
              "air_warning": warning_condition[0],
            },
            "meta": {
                "msg": "登录成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@warn.route("/api/door", methods=['GET'])
def warn_door():
    room_num = user.roomnum
    warn_student = Dormcondition.query.filter(Dormcondition.address.contains(room_num)).all()
    condition = []
    warning_condition = []
    if warn_student is not None:
        for w in warn_student:
            if w.door == 1:
                condition.append("门未关")
                warning_condition.append(True)
            else:
                condition.append("正常")
                warning_condition.append(False)
        response_consume_dic = {
            "data": {
              "door_condition": condition[0],
              "door_warning": warning_condition[0],
            },
            "meta": {
                "msg": "登录成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)

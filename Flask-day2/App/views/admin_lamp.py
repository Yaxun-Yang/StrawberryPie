from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from ..models import Information, Consumption, Environment, Plant, Login, Admin, Bedroom, Rules
from ..requestuser.User import User
from App.ext import db
from App.views.first import user
admin_lamp = Blueprint('admin_lamp', __name__)


@admin_lamp.route("/api/dorms", methods=['GET'])
def get_no_close_lamp():
    print("请求")
    page_num = request.args.get('pagenum')
    page_size = request.args.get('pagesize')
    room_number = user.roomnum
    bedrooms = Bedroom.query.filter(Bedroom.roomnumber.contains(room_number)).all()
    page_bedroom = Bedroom.query.paginate(page=int(page_num), per_page=int(page_size), error_out=False)
    # information = Information.query.filter(Information.roomnumber.contains(room_number)).all()
    rule = Rules.query.filter_by(roomnumber=room_number).first()

    # students = []
    # for i in information:
    #     students.append(i.username)
    # students_str = "、".join(students)
    dorms = []
    for b in page_bedroom.items:
        information = Information.query.filter(Information.roomnumber.contains(b.roomnumber)).all()
        students = []
        for i in information:
            students.append(i.username)
        students_str = "、".join(students)
        dorms.append({
            "dorm": b.roomnumber,
            "student": students_str
        })
    print(students_str)
    response_consume_dic = {
        "data": {
            "totalpage": len(bedrooms),
            "pagenum": page_num,
            "dorms": dorms,
            "close_time": rule.lampclosetime,
            "remind_time": rule.lampremindtime
        },
        "meta": {
            "msg": "登录成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@admin_lamp.route("/api/lamp/closetime/<close_time>", methods=['PUT'])
def fix_lamp_close_time(close_time):
    room_number = user.roomnum
    rule = Rules.query.filter(Rules.roomnumber.contains(room_number)).all()
    for r in rule:
        r.lampclosetime = close_time
    db.session.commit()
    response_consume_dic = {
        "meta": {
            "msg": "登录成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@admin_lamp.route("/api/lamp/remindtime/<remind_time>", methods=['PUT'])
def fix_lamp_remind_time(remind_time):
    room_number = user.roomnum
    rule = Rules.query.filter(Rules.roomnumber.contains(room_number)).all()
    for r in rule:
        r.lampremindtime = remind_time
    db.session.commit()
    response_consume_dic = {
        "meta": {
            "msg": "登录成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)
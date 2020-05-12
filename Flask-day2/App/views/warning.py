from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from ..models import Dormcondition, Bedroom, Toilet, Balcony, Environment
from App.ext import db
from App.views.first import user
warn = Blueprint('warn', __name__)


@warn.route("/api/air", methods=['GET'])
def warn_air():
    room_num = user.roomnum
    room1 = Bedroom.query.filter_by(roomnumber=room_num).first()
    room2 = Toilet.query.filter_by(roomnumber=room_num).first()
    room3 = Balcony.query.filter_by(roomnumber=room_num).first()
    environment = Environment.query.order_by(-Environment.id).first()
    if room1.lampcon == 1:
        light1 = True
    else:
        light1 = False
    if room1.airconditioncon == 1:
        air1 = True
    else:
        air1 = False
    if room1.watercon == 1:
        water1 = True
    else:
        water1 = False
    if room1.doorcon == 1:
        door1 = True
    else:
        door1 = False
    if room2.lampcon == 1:
        light2 = True
    else:
        light2 = False
    if room3.lampcon == 1:
        light3 = True
    else:
        light3 = False
    if int(environment.indoortem) > room1.temlow & int(environment.indoortem) < room1.temhigh:
        tem1 = True
    else:
        tem1 = False
    if int(environment.indoortem) > room2.temlow & int(environment.indoortem) < room2.temhigh:
        tem2 = True
    else:
        tem2 = False
    if int(environment.indoortem) > room3.temlow & int(environment.indoortem) < room3.temhigh:
        tem3 = True
    else:
        tem3 = False
    if int(environment.indoorhum) > room1.humlow & int(environment.indoorhum) < room1.humhigh:
        hum1 = True
    else:
        hum1 = False
    if int(environment.indoorhum) > room2.humlow & int(environment.indoorhum) < room2.humhigh:
        hum2 = True
    else:
        hum2 = False
    if int(environment.indoorhum) > room3.humlow & int(environment.indoorhum) < room3.humhigh:
        hum3 = True
    else:
        hum3 = False
    if room1.doorwarn == 1:
        doorclosed = False
    else:
        doorclosed = True
    response_dic = {
        "data": {
            "value1": True,
            "wifi1OK": True,
            "value2": True,
            "wifi2OK": True,
            "value3": True,
            "wifi3OK": True,
            "temp1": tem1,
            "hum1": hum1,
            "light1": light1,
            "door1": door1,
            "doorClosed": doorclosed,
            "air1": air1,
            "water1": water1,
            "temp2": tem2,
            "hum2": hum2,
            "light2": light2,
            "temp3": tem3,
            "hum3": hum3,
            "light3": light3
        },
        "meta": {
            "msg": "查询成功",
            "status": 200
        }
    }
    return jsonify(response_dic)


@warn.route("/api/manage", methods=['GET'])
def manage_information():
    room_num = user.roomnum
    room1 = Bedroom.query.filter_by(roomnumber=room_num).first()
    room2 = Toilet.query.filter_by(roomnumber=room_num).first()
    room3 = Balcony.query.filter_by(roomnumber=room_num).first()
    environment = Environment.query.order_by(-Environment.id).first()
    if room1.lampcon == 1:
        light1 = True
    else:
        light1 = False
    if room1.airconditioncon == 1:
        air1 = True
    else:
        air1 = False
    if room1.watercon == 1:
        water1 = True
    else:
        water1 = False
    if room1.doorcon == 1:
        door1 = True
    else:
        door1 = False
    if room2.lampcon == 1:
        light2 = True
    else:
        light2 = False
    if room3.lampcon == 1:
        light3 = True
    else:
        light3 = False
    # if int(environment.indoortem) > 30:
    #     hum1 = True
    # else:
    #     hum1 = False
    # if int(environment.indoortem) > 30:
    #     temp1 = True
    # else:
    #     temp1 = False
    if int(environment.indoortem) > room1.temlow & int(environment.indoortem) < room1.temhigh:
        tem1 = True
    else:
        tem1 = False
    if int(environment.indoortem) > room2.temlow & int(environment.indoortem) < room2.temhigh:
        tem2 = True
    else:
        tem2 = False
    if int(environment.indoortem) > room3.temlow & int(environment.indoortem) < room3.temhigh:
        tem3 = True
    else:
        tem3 = False
    if int(environment.indoorhum) > room1.humlow & int(environment.indoorhum) < room1.humhigh:
        hum1 = True
    else:
        hum1 = False
    if int(environment.indoorhum) > room2.humlow & int(environment.indoorhum) < room2.humhigh:
        hum2 = True
    else:
        hum2 = False
    if int(environment.indoorhum) > room3.humlow & int(environment.indoorhum) < room3.humhigh:
        hum3 = True
    else:
        hum3 = False
    response_dic = {
        "data": {
            "value1": True,
            "value2": True,
            "value3": True,
            "temp1": tem1,
            "hum1": hum1,
            "light1": light1,
            "door1": door1,
            "air1": air1,
            "water1": water1,
            "temp2": tem2,
            "hum2": hum2,
            "light2": light2,
            "temp3": tem3,
            "hum3": hum3,
            "light3": light3
        },
        "meta": {
            "msg": "查询成功",
            "status": 200
        }
    }
    return jsonify(response_dic)


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

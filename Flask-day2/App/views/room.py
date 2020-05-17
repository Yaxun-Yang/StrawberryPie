import json

from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify, url_for
from ..models import Bedroom, Environment, Toilet, Balcony, Information
from ..requestuser.User import User
from .first import user as use_en
from App.ext import db
from .environment.get_environment import insert_environment
from .first import userList
from App.token.authorization_token import authorization_token

room = Blueprint('room', __name__)


def get_environment():
    insert_environment()
    username = use_en.username
    roomnum = use_en.roomnum
    print("pet" + roomnum)
    environment = Environment.query.order_by(-Environment.id).first()
    return environment


@room.route('/api/room1')
def get_bedroom_information():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        bedrooms = Bedroom.query.filter_by(roomnumber=roomnumber).all()
        environment = get_environment()
        set_tem = [bedrooms[0].temlow, bedrooms[0].temhigh]
        set_hum = [bedrooms[0].humlow, bedrooms[0].humhigh]
        bedroom_result = {
            'temp': environment.indoortem,
            'humid': environment.indoorhum,
            'value': bedrooms[0].devnum,
            'value1': bedrooms[0].lamplight,
            "value2": True,
            'value3': bedrooms[0].airconditiontem,
            "value4": True,
            'value5': bedrooms[0].watertemp,
            "value6": True
        }
        if bedrooms[0].doorcon == 1:
            door_value = True
        else:
            door_value = False
        if bedrooms[0].lampcon == 1:
            bedroom_result["value2"] = True
        else:
            bedroom_result["value2"] = False

        if bedrooms[0].airconditioncon == 1:
            bedroom_result["value4"] = True
        else:
            bedroom_result["value4"] = False

        if bedrooms[0].watercon == 1:
            bedroom_result["value6"] = True
        else:
            bedroom_result["value6"] = False

        response_consume_dic = {
            "data": {
                'temp': environment.indoortem,
                'humid': environment.indoorhum,
                'value': bedroom_result['value'],
                'value1': bedroom_result['value1'],
                'value2': bedroom_result['value2'],
                'value3': bedroom_result['value3'],
                'value4': bedroom_result['value4'],
                'value5': bedroom_result['value5'],
                'value6': bedroom_result['value6'],
                "setTemp": set_tem,
                "setHumid": set_hum,
                "door_value": door_value
            },
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/door/change/<door_value>", methods=['PUT'])
def room1_door_con_change(door_value):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Bedroom.query.filter_by(roomnumber=roomnumber).first()
        if door_value == 'true':
            change.doorcon = 1
        else:
            change.doorcon = 0
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/templight/change/<light>", methods=['PUT'])
def change_temp_light(light):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Bedroom.query.filter_by(roomnumber=roomnumber).first()
        change.lamplight = light
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/aircondition/change/<tem>", methods=['PUT'])
def change_aircondition(tem):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Bedroom.query.filter_by(roomnumber=roomnumber).first()
        change.airconditiontem = tem
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/water/change/<watertem>", methods=['PUT'])
def change_water(watertem):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Bedroom.query.filter_by(roomnumber=roomnumber).first()
        change.watertemp = watertem
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room2")
def get_toilet_information():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        toilet = Toilet.query.filter_by(roomnumber=roomnumber).all()
        set_tem = [toilet[0].temlow, toilet[0].temhigh]
        set_hum = [toilet[0].humlow, toilet[0].humhigh]
        environment = get_environment()
        bedroom_result = {
            'temp': environment.indoortem,
            'humid': environment.indoorhum,
            'value': toilet[0].devnum,
            'value1': toilet[0].lamplight,
            "value2": True
        }

        if toilet[0].lampcon == 1:
            bedroom_result["value2"] = True
        else:
            bedroom_result["value2"] = False

        response_consume_dic = {
            "data": {
                'temp': environment.indoortem,
                'humid': environment.indoorhum,
                'value': bedroom_result['value'],
                'value1': bedroom_result['value1'],
                'value2': bedroom_result['value2'],
                "setTemp": set_tem,
                "setHumid": set_hum
            },
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room2/templight/change/<light>", methods=['PUT'])
def change_room2_light(light):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Toilet.query.filter_by(roomnumber=roomnumber).first()
        change.lamplight = light
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room3")
def get_balcony_information():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        balcony = Balcony.query.filter_by(roomnumber=roomnumber).all()
        set_tem = [balcony[0].temlow, balcony[0].temhigh]
        set_hum = [balcony[0].humlow, balcony[0].humhigh]
        environment = get_environment()
        bedroom_result = {
            'temp': environment.indoortem,
            'humid': environment.indoorhum,
            'value': balcony[0].devnum,
            'value1': balcony[0].lamplight,
            "value2": True
        }

        if balcony[0].lampcon == 1:
            bedroom_result["value2"] = True
        else:
            bedroom_result["value2"] = False

        response_consume_dic = {
            "data": {
                'temp': environment.indoortem,
                'humid': environment.indoorhum,
                'value': bedroom_result['value'],
                'value1': bedroom_result['value1'],
                'value2': bedroom_result['value2'],
                "setTemp": set_tem,
                "setHumid": set_hum
            },
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room3/templight/change/<light>", methods=['PUT'])
def change_room3_light(light):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Balcony.query.filter_by(roomnumber=roomnumber).first()
        change.lamplight = light
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/lightcon/change/<lightcon>", methods=['PUT'])
def change_room1_lightcon(lightcon):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Bedroom.query.filter_by(roomnumber=roomnumber).first()
        count = change.devnum
        if lightcon == 'true':
            light = 1
            count = count + 1
        else:
            light = 0
            count = count - 1
        change.lampcon = light
        change.devnum = count
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/aircon/change/<aircon>", methods=['PUT'])
def change_room1_aircon(aircon):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Bedroom.query.filter_by(roomnumber=roomnumber).first()
        count = change.devnum
        air = 0
        if aircon == 'true':
            air = 1
            count = count + 1
        else:
            air = 0
            count = count - 1
        change.airconditioncon = air
        change.devnum = count
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/watercon/change/<watercon>", methods=['PUT'])
def change_room1_watercon(watercon):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Bedroom.query.filter_by(roomnumber=roomnumber).first()
        count = change.devnum
        water = 0
        if watercon == 'true':
            water = 1
            count = count + 1
        else:
            water = 0
            count = count - 1
        print(count)
        change.watercon = water
        change.devnum = count
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room2/lightcon/change/<lightcon>", methods=['PUT'])
def change_room2_lightcon(lightcon):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Toilet.query.filter_by(roomnumber=roomnumber).first()
        count = change.devnum
        if lightcon == 'true':
            light = 1
            count = count + 1
        else:
            light = 0
            count = count - 1
        change.lampcon = light
        change.devnum = count
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room3/lightcon/change/<lightcon>", methods=['PUT'])
def change_room3_lightcon(lightcon):
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        change = Balcony.query.filter_by(roomnumber=roomnumber).first()
        count = change.devnum
        if lightcon == 'true':
            light = 1
            count = count + 1
        else:
            light = 0
            count = count - 1
        change.lampcon = light
        change.devnum = count
        db.session.commit()
        response_consume_dic = {
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/warning/door", methods=['GET'])
def warning_door():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        roomnumber = user.roomnum
        print("已接受到门未🔒警告信息")
        # 这里需要发短信通知用户 已列出 电话，用户名，宿舍号信息
        information = Information.query.filter_by(username=user.username).first()
        phone_number = information.phonenum
        student_name = information.username
        student_roomnumber = information.roomnumber

        response_consume_dic = {
            "meta": {
                "msg": "发送成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@room.route("/api/room1/tem")
def change_room1_tem():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        low_tem = request.values.get("low_temp")
        high_tem = request.args.get("high_temp")
        room1 = Bedroom.query.filter_by(roomnumber=user.roomnum).first()
        room1.temlow = low_tem
        room1.temhigh = high_tem
        db.session.commit()
        response = {
            "meta": {
                "msg": "修改成功",
                "status": 200
            }
        }
        return jsonify(response)


@room.route("/api/room1/hum")
def change_room1_hum():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        low_hum = request.values.get("low_hum")
        high_hum = request.args.get("high_hum")
        room1 = Bedroom.query.filter_by(roomnumber=user.roomnum).first()
        room1.humlow = low_hum
        room1.humhigh = high_hum
        db.session.commit()
        response = {
            "meta": {
                "msg": "修改成功",
                "status": 200
            }
        }
        return jsonify(response)


@room.route("/api/room2/tem")
def change_room2_tem():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        low_tem = request.values.get("low_temp")
        high_tem = request.args.get("high_temp")
        room1 = Toilet.query.filter_by(roomnumber=user.roomnum).first()
        room1.temlow = low_tem
        room1.temhigh = high_tem
        db.session.commit()
        response = {
            "meta": {
                "msg": "修改成功",
                "status": 200
            }
        }
        return jsonify(response)


@room.route("/api/room2/hum")
def change_room2_hum():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        low_hum = request.values.get("low_hum")
        high_hum = request.args.get("high_hum")
        room1 = Toilet.query.filter_by(roomnumber=user.roomnum).first()
        room1.humlow = low_hum
        room1.humhigh = high_hum
        db.session.commit()
        response = {
            "meta": {
                "msg": "修改成功",
                "status": 200
            }
        }
        return jsonify(response)


@room.route("/api/room3/tem")
def change_room3_tem():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        low_tem = request.values.get("low_temp")
        high_tem = request.args.get("high_temp")
        room1 = Balcony.query.filter_by(roomnumber=user.roomnum).first()
        room1.temlow = low_tem
        room1.temhigh = high_tem
        db.session.commit()
        response = {
            "meta": {
                "msg": "修改成功",
                "status": 200
            }
        }
        return jsonify(response)


@room.route("/api/room3/hum")
def change_room3_hum():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
        low_hum = request.values.get("low_hum")
        high_hum = request.args.get("high_hum")
        room1 = Balcony.query.filter_by(roomnumber=user.roomnum).first()
        room1.humlow = low_hum
        room1.humhigh = high_hum
        db.session.commit()
        response = {
            "meta": {
                "msg": "修改成功",
                "status": 200
            }
        }
        return jsonify(response)






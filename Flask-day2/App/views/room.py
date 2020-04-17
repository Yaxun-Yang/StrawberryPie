import json

from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify, url_for
from ..models import Bedroom, Environment, Toilet, Balcony, Information
from ..requestuser.User import User
from .first import user
from App.ext import db
from .environment.get_environment import insert_environment

room = Blueprint('room', __name__)


def get_environment():
    insert_environment()
    username = user.username
    roomnum = user.roomnum
    print("pet" + roomnum)
    environment = Environment.query.order_by(-Environment.id).first()
    return environment


@room.route('/api/room1')
def get_bedroom_information():
    roomnumber = user.roomnum
    bedrooms = Bedroom.query.filter_by(roomnumber='新二舍102').all()
    environment = get_environment()
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
            "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE1MTI1NDQyOTksImV4cCI6MTUxMjYzMDY5OX0.eGrsrvwHm-tPsO9r_pxHIQ5i5L1kX9RX444uwnRGaIM"
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@room.route("/api/room1/templight/change/<light>", methods=['PUT'])
def change_temp_light(light):
    roomnumber = user.roomnum
    change = Bedroom.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    change = Bedroom.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    change = Bedroom.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    toilet = Toilet.query.filter_by(roomnumber='新二舍102').all()
    # print(roomnumber)
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
            "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE1MTI1NDQyOTksImV4cCI6MTUxMjYzMDY5OX0.eGrsrvwHm-tPsO9r_pxHIQ5i5L1kX9RX444uwnRGaIM"
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@room.route("/api/room2/templight/change/<light>", methods=['PUT'])
def change_room2_light(light):
    roomnumber = user.roomnum
    change = Toilet.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    balcony = Balcony.query.filter_by(roomnumber='新二舍102').all()
    # print(roomnumber)
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
            "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE1MTI1NDQyOTksImV4cCI6MTUxMjYzMDY5OX0.eGrsrvwHm-tPsO9r_pxHIQ5i5L1kX9RX444uwnRGaIM"
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@room.route("/api/room3/templight/change/<light>", methods=['PUT'])
def change_room3_light(light):
    roomnumber = user.roomnum
    change = Balcony.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    change = Bedroom.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    change = Bedroom.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    change = Bedroom.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    change = Toilet.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    change = Balcony.query.filter_by(roomnumber='新二舍102').first()
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
    roomnumber = user.roomnum
    print("已接受到门未🔒警告信息")

    #这里需要发短信通知用户 已列出 电话，用户名，宿舍号信息
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



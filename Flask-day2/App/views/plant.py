import json

from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify

from .environment.get_environment import insert_environment
from ..models import Information, Consumption, Environment, Plant
from App.ext import db
from App.warning.catch_plant import catch_plant
from .first import userList
from App.token.authorization_token import authorization_token

resplant = Blueprint('resplant', __name__)


def get_environment():
    insert_environment()
    environment = Environment.query.order_by(-Environment.id).first()
    return environment


def get_plant_list():
    user_token = request.headers.get("Authorization")
    # print(user_token)
    user_plant = authorization_token(userList, user_token)
    # print(user_plant.roomnum)
    if user_plant is not None:
        plants = Plant.query.filter_by(roomnumber=user_plant.roomnum).all()
        # 查询plant
        plant_type = Plant.query.filter_by(roomnumber=user_plant.roomnum).with_entities(Plant.plantname).distinct().all()
        plant_list = []
        for p in plants:
            time = p.watertime.split('+')
            time_list = []
            i = 0
            for t in time:
                i = i + 1
                time_list.append(
                    {
                        'time': t,
                        'timeId': i
                    }
                )
            plant_list.append(
                {
                    'plantName': p.plantname,
                    'plantId': p.id,
                    'timeList': time_list,
                    'percent': p.percent,
                    'amount': p.amount,
                    'imagUrl': p.imgurl
                }
            )
        return plant_list
    else:
        return None


@resplant.route('/api/plant', methods=['GET'])
def plant():
    environment = get_environment()
    plant_list = get_plant_list()
    response_consume_dic = {
        "data": {
            'indoor_temperature': environment.indoortem,
            'outdoor_temperature': environment.outdoortem,
            'indoor_humidity': environment.indoorhum,
            'outdoor_humidity': environment.outdoorhum,
            'plantList': plant_list
        },
        "meta": {
            "msg": "查询成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@resplant.route('/api/plant/<plantId>', methods=['DELETE'])
def delete_plant(plantId):
    plant_delete = Plant.query.filter_by(id=plantId).all()
    db.session.delete(plant_delete[0])
    db.session.commit()
    environment = get_environment()
    plant_list = get_plant_list()
    response_consume_dic = {
        "data": {
            'indoor_temperature': environment.indoortem,
            'outdoor_temperature': environment.outdoortem,
            'indoor_humidity': environment.indoorhum,
            'outdoor_humidity': environment.outdoorhum,
            'plantList': plant_list
        },
        "meta": {
            "msg": "查询成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@resplant.route('/api/plant/<plantId>/time', methods=['POST'])
def new_water_time(plantId):
    plants = Plant.query.filter_by(id=plantId).all()
    time_list = []
    for p in plants:
        time = p.watertime.split('+')
        i = 0
        for t in time:
            i = i + 1
            time_list.append(
                {
                    'time': t,
                    'timeId': i
                }
            )
        i = i + 1
        time_list.append(
            {
                'time': '',
                'timeId': i
            }
        )
    response_consume_dic = {
        "data": {
            'timeList': time_list,
            'plantId': plantId
        },
        "meta": {
            "msg": "查询成功",
            "status": 201
        }
    }
    return jsonify(response_consume_dic)


@resplant.route('/api/users/<plantId>/amount/<timeId>', methods=['DELETE', 'PUT'])
def delete_water_time(plantId, timeId):
    if request.method == 'DELETE':
        plants = Plant.query.filter_by(id=plantId).all()
        time_pre = plants[0].watertime.split('+')
        print(time_pre)
        del time_pre[int(timeId) - 1]
        time_list = []
        new_time = ''
        for t in time_list:
            new_time = new_time + t
        change_plant = Plant.query.filter_by(id=plantId).first()
        change_plant.watertime = new_time
        db.session.commit()
        for p in plants:
            i = 0
            for t in time_pre:
                i = i + 1
                time_list.append(
                    {
                        'time': t,
                        'timeId': i
                    }
                )
        response_consume_dic = {
            "data": {
                'timeList': time_list,
                'plantId': plantId
            },
            "meta": {
                "msg": "删除成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)
    else:
        print('plant amount')
        change_plant = Plant.query.filter_by(id=plantId).first()
        change_plant.amount = timeId
        db.session.commit()
        plant_list = get_plant_list()
        response_consume_dic = {
            "data": {
                'plantList': plant_list
            },
            "meta": {
                "msg": "修改成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@resplant.route('/api/users/<plantId>/time/<time>', methods=['PUT'])
def change_water_time(plantId, time):
    print("plantId" + plantId)
    change_plant = Plant.query.filter_by(id=plantId).first()
    change_plant.watertime = change_plant.watertime + '+' + time
    db.session.commit()
    print(change_plant.watertime)
    environment = get_environment()
    plant_list = get_plant_list()
    response_consume_dic = {
        "data": {
            'indoor_temperature': environment.indoortem,
            'outdoor_temperature': environment.outdoortem,
            'indoor_humidity': environment.indoorhum,
            'outdoor_humidity': environment.outdoorhum,
            'plantList': plant_list
        },
        "meta": {
            "msg": "查询成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@resplant.route("/api/plant/add", methods=['POST'])
def add_plant():
    user_token = request.headers.get("Authorization")
    user_plant = authorization_token(userList, user_token)
    if user_plant is not None:
        new_plant = catch_plant()
        if new_plant is not None:
            judge = True
        else:
            judge = False
        if judge:
            plane_name = new_plant.get("plant_name")
            img_url = new_plant.get("img_url")
            plane_add = Plant(user_plant.roomnum, plane_name, img_url, "80", "20", "10:00:00")
            db.session.add(plane_add)
            db.session.commit()
            plant_list = get_plant_list()
            response = {
                "data": {
                    "plantList": plant_list
                },
                "meta": {
                    "msg": "添加成功",
                    "status": 201
                }
            }
            return jsonify(response)
        else:
            response = {
                "meta": {
                    "msg": "未检测到新植物",
                    "status": 200
                }
            }
            return jsonify(response)
    else:
        response = {
            "meta": {
                "msg": "未登录",
                "status": 200
            }
        }
        return jsonify(response)

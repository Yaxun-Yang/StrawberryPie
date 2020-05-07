from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from ..models import Information, Consumption, Environment, Plant, Pet
from App.ext import db
from .environment.get_environment import insert_environment
from App.warning.catch_pet import catch_pet
from .first import userList
from App.token.authorization_token import authorization_token

pet = Blueprint('pet', __name__)


def get_pet_list():
    user_token = request.headers.get("Authorization")
    print(user_token)
    user_pet = authorization_token(userList, user_token)
    if user_pet is not None:
        pets = Pet.query.filter_by(roomnumber=user_pet.roomnum).all()
        # 查询plant
        pet_type = Pet.query.filter_by(roomnumber=user_pet.roomnum).with_entities(Pet.petname).distinct().all()
        pet_list = []
        for p in pets:
            time = p.feedtime.split('+')
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
            pet_list.append(
                {
                    'petName': p.petname,
                    'petId': p.id,
                    'timeList': time_list,
                    'percent': p.percent,
                    'amount': p.amount,
                    'imagUrl': p.imgurl
                }
            )
        return pet_list
    else:
        return None


def get_environment():
    insert_environment()
    # username = user.username
    # roomnum = user.roomnum
    # print("pet" + roomnum)
    environment = Environment.query.order_by(-Environment.id).first()
    return environment


@pet.route('/api/pet', methods=['GET', 'POST'])
def pet_information():
    environment = get_environment()
    pet_list = get_pet_list()
    if request.method == 'POST':
        response_consume_dic = {
            "data": {
                'indoor_temperature': environment.indoortem,
                'outdoor_temperature': environment.outdoortem,
                'indoor_humidity': environment.indoorhum,
                'outdoor_humidity': environment.outdoorhum,
                'petList': pet_list
            },
            "meta": {
                "msg": "植物创建成功",
                "status": 201
            }
        }
        return jsonify(response_consume_dic)
    else:
        response_consume_dic = {
            "data": {
                'indoor_temperature': environment.indoortem,
                'outdoor_temperature': environment.outdoortem,
                'indoor_humidity': environment.indoorhum,
                'outdoor_humidity': environment.outdoorhum,
                'petList': pet_list
            },
            "meta": {
                "msg": "查询成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@pet.route('/api/pet/<petId>', methods=['DELETE'])
def remove_pet(petId):
    p = Pet.query.filter_by(id=petId).all()
    db.session.delete(p[0])
    db.session.commit()
    environment = get_environment()
    pet_list = get_pet_list()
    response_consume_dic = {
        "data": {
            'indoor_temperature': environment.indoortem,
            'outdoor_temperature': environment.outdoortem,
            'indoor_humidity': environment.indoorhum,
            'outdoor_humidity': environment.outdoorhum,
            'petList': pet_list
        },
        "meta": {
            "msg": "删除成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@pet.route('/api/pet/<petId>/time', methods=['POST'])
def new_feed_time(petId):
    print('pet feed time')
    pets = Pet.query.filter_by(id=petId).all()
    time_list = []
    for p in pets:
        time = p.feedtime.split('+')
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
            'petId': petId
        },
        "meta": {
            "msg": "查询成功",
            "status": 201
        }
    }
    return jsonify(response_consume_dic)


@pet.route('/api/users/<petId>/time/<timeId>', methods=['PUT', 'DELETE'])
def feed_time(petId, timeId):
    if request.method == 'DELETE':
        pets = Pet.query.filter_by(id=petId).all()
        time_pre = pets[0].feedtime.split('+')
        print(time_pre)
        del time_pre[int(timeId)-1]
        time_list = []
        new_time = ''
        for t in time_list:
            new_time = new_time + t
        change_plant = Pet.query.filter_by(id=petId).first()
        change_plant.feedtime = new_time
        db.session.commit()
        for p in pets:
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
                'petId': petId
            },
            "meta": {
                "msg": "删除成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)


@pet.route('/api/pet/<petId>/amount/<amount>', methods=['PUT'])
def change_pet_mount(petId, amount):
    change_pet = Pet.query.filter_by(id=petId).first()
    change_pet.amount = amount
    db.session.commit()
    pet_list = get_pet_list()
    response_consume_dic = {
        "data": {
            'petList': pet_list
        },
        "meta": {
            "msg": "修改成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@pet.route('/api/pet/<petId>/time/<time>', methods=['PUT'])
def change_pet_feed_time(petId, time):
    print(petId)
    change_pet = Pet.query.filter_by(id=petId).first()
    change_pet.feedtime = change_pet.feedtime + '+' + time
    db.session.commit()
    print(change_pet.watertime)
    environment = get_environment()
    pet_list = get_pet_list()
    response_consume_dic = {
        "data": {
            'indoor_temperature': environment.indoortem,
            'outdoor_temperature': environment.outdoortem,
            'indoor_humidity': environment.indoorhum,
            'outdoor_humidity': environment.outdoorhum,
            'petList': pet_list
        },
        "meta": {
            "msg": "查询成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@pet.route("/api/pet/add", methods=['POST'])
def add_pet():
    new_pet = catch_pet()
    if new_pet is not None:
        judge = True
    else:
        judge = False
    if judge:
        pet_name = new_pet.get("pet_name")
        img_url = new_pet.get("img_url")
        pet_add = Pet("新二舍102", pet_name, img_url, "20", "70", "10:00:00")
        db.session.add(pet_add)
        db.session.commit()
        print(pet_name)
        pet_list = get_pet_list()
        response = {
            "data": {
                "petList": pet_list
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
                "msg": "未检测到新宠物",
                "status": 200
            }
        }
        return jsonify(response)

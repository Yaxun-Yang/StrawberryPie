from flask import jsonify

from App.models import Environment, Pet, Plant
from App.views.first import user


def get_pet_information():
    username = user.username
    roomnum = user.roomnum
    print("pet" + roomnum)
    # print(username)
    environment = Environment.query.order_by(-Environment.id).first()
    # print(environment.id)
    # 查询plant全部信息
    pets = Pet.query.filter_by(roomnumber='新二舍102').all()
    # 查询plant
    pet_type = Plant.query.filter_by(roomnumber='新二舍102').with_entities(Pet.petname).distinct().all()
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
                'petId': p.id,
                'timeList': time_list,
                'percent': p.percent,
                'amount': p.amount,
                'imagUrl': p.imgurl
            }
        )
    response_consume_dic = {
        "data": {
            'indoor_temperature': environment.indoortem,
            'outdoor_temperature': environment.outdoortem,
            'indoor_humidity': environment.indoorhum,
            'outdoor_humidity': environment.outdoorhum,
            'petList': pet_list,
            "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE1MTI1NDQyOTksImV4cCI6MTUxMjYzMDY5OX0.eGrsrvwHm-tPsO9r_pxHIQ5i5L1kX9RX444uwnRGaIM"
        },
        "meta": {
            "msg": "查询成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)

# "information": [
#                     {
#                         "water": consume_result[0].get('water'),
#                         "electricity": consume_result[0].get('electricity'),
#                         "date": consume_result[0].get('date')
#                     }
#                 ],

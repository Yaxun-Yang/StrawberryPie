from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from ..models import Information, Consumption, Environment, Plant, Login, Admin
from ..requestuser.User import User
from App.ext import db
from App.token.build_token import Token
blue = Blueprint('blue', __name__)


user = User("1", "2", " ")
userList = []


@blue.route('/api/login', methods=['GET', 'POST'])
def try_vue():
    getUsername = request.get_json()['username']
    getPassword = request.get_json()['password']
    tokenprogramer = Token('api_secret具体值', 'project_code具体值', 'account具体值')
    token = tokenprogramer.get_token()
    login = Login.query.filter_by(username=getUsername, password=getPassword).all()
    print(login[0].authetic)
    print(login[0].name)
    if login[0].authetic == 1:
        print("管理员登录")
        admin = Admin.query.filter_by(name=login[0].name).first()
        response_dic = {
            "data": {
                "manager":
                {
                    'name': admin.name,
                    'id': admin.adminid,
                    'type': admin.type,
                    'dept': admin.dept,
                    'building': admin.building,
                    'floor': admin.floor,
                    'room': admin.room,
                    'people': admin.people,
                    'address': admin.address
                },
                "token": token
            },
            "meta": {
                "msg": "登录成功",
                "status": 200
            },
            "status": "admin"
        }
        user.update_user(getUsername, admin.address, token)
        userList.append(user)
        return jsonify(response_dic)
    else:
        print("用户登录")
        # print(getUsername)
        information = Information.query.filter_by(stuid=getUsername).all()
        # print(information)
        resData = []
        for x in information:
            resData.append({
                'username': x.username,
                'classnum': x.classnum,
                'roomnumber': x.roomnumber,
                'roommate': x.roommate,
                'img': x.img,
                'stuid': x.stuid,
                'college': x.college,
                "stutype": x.stutype,
                'phonenum': x.phonenum,
                'time': x.time
            })
        print("information" + resData[0]["roomnumber"])

        user.update_user(resData[0]["username"], resData[0]["roomnumber"], token)
        userList.append(user)
        response_dic = {
            "data": {
                "id": 500,
                "rid": 0,
                "username": resData[0]["username"],
                "mobile": "123",
                "email": "123@qq.com",
                "classnum": resData[0]["classnum"],
                "roomnumber": resData[0]["roomnumber"],
                "roommate": resData[0]["roommate"],
                "img": resData[0]["img"],
                'stuid': resData[0]["stuid"],
                'college': resData[0]["college"],
                "stutype": resData[0]["stutype"],
                'phonenum': resData[0]["phonenum"],
                'time': resData[0]["time"],
                "token": token
            },
            "meta": {
                "msg": "登录成功",
                "status": 200
            },
            "status": "student"
        }
        return jsonify(response_dic)


@blue.route("/api/admin/reset_password", methods=['GET'])
def reset_password():
    new_password = request.args.get('newpassword')
    print(new_password)
    print(user.username)
    login = Login.query.filter_by(username="0102").all()
    login[0].password = new_password
    db.session.commit()
    response_consume_dic = {
        "meta": {
            "msg": "登录成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@blue.route('/api/information', methods=['GET', 'POST', 'PUT'])
def get_information():
    page_num = request.args.get('pagenum')
    page_size = request.args.get('pagesize')
    dateRange = request.args.getlist('dateRange[]')
    username = user.username
    roomnum = user.roomnum
    if not dateRange:
        consume_all = Consumption.query.filter_by(roomnum='新二舍102').all()
        consume = Consumption.query.filter(Consumption.roomnum.contains('新二舍102')).paginate(page=int(page_num), per_page=int(page_size), error_out=False)
        total_page = len(consume_all)
        consume_result = []
        for x in consume.items:
            print(x.water)
            consume_result.append({
                'water': x.water,
                'electricity': x.electricity,
                'date': x.date
            })
        response_consume_dic = {
            "data": {
                "total": total_page,
                "pagenum": page_num,
                "information": consume_result
            },
            "meta": {
                "msg": "登录成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)
    else:
        print("have")
        consume = Consumption.query.filter_by(roomnum='新二舍102').filter(Consumption.date >= dateRange[0]) .filter(Consumption.date <= dateRange[1]).paginate(page=int(page_num), per_page=int(page_size), error_out=False)
        total_page = len(consume.items)
        consume_result = []
        for x in consume.items:
            print(x.water)
            consume_result.append({
                'water': x.water,
                'electricity': x.electricity,
                'date': x.date
            })

        response_consume_dic = {
            "data": {
                "total": total_page,
                "pagenum": page_num,
                "information": consume_result
            },
            "meta": {
                "msg": "登录成功",
                "status": 200
            }
        }
        return jsonify(response_consume_dic)







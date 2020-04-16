from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from sqlalchemy import text
from ..models import Information, Consumption, Environment, Plant, Login, Admin, Bedroom, Rules
from App.ext import db
from App.views.first import user
students = Blueprint('students', __name__)


@students.route("/api/users", methods=['GET'])
def admin_students():
    room_number = user.roomnum
    query = request.args.get('query')
    select = request.args.get('select')
    page_num = request.args.get('pagenum')
    page_size = request.args.get('pagesize')
    information = Information.query.filter(Information.roomnumber.contains(room_number) if room_number is not None else text(""),
                                           Information.username.contains(query) if select == '1' else text(""),
                                           Information.roomnumber.contains(query) if select == '2' else text(""),
                                           Information.classnum.contains(query) if select == '3' else text("")).all()
    total = len(information)
    # page_information = Information.query.paginate(page=int(page_num), per_page=int(page_size), error_out=False)
    page_information = Information.query.filter(Information.roomnumber.contains(room_number) if room_number is not None else text(""),
                                           Information.username.contains(query) if select == '1' else text(""),
                                           Information.roomnumber.contains(query) if select == '2' else text(""),
                                           Information.classnum.contains(query) if select == '3' else text("")).paginate(page=int(page_num), per_page=int(page_size), error_out=False)
    student_list = []
    for i in page_information.items:
        student_list.append({
            "dorm": i.roomnumber,
            "name": i.username,
            "type": i.stutype,
            "class": i.classnum,
            "number": i.stuid
        })
    response_consume_dic = {
        "data": {
            "users": student_list,
            "total": total
        },
        "meta": {
            "msg": "登录成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)

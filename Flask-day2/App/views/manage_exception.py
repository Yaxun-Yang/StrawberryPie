from flask import Blueprint, request, jsonify
from ..models import Warn
from App.views.first import user
exception = Blueprint('exception', __name__)


@exception.route("/api/exceptions", methods=['GET'])
def manage_exceptions():
    room_number = user.roomnum
    query = request.args.get('query')
    page_num = request.args.get('pagenum')
    page_size = request.args.get('pagesize')
    exception_data = Warn.query.filter(Warn.address.contains(room_number)).all()
    total = len(exception_data)
    page_exception = Warn.query.filter(Warn.address.contains(room_number)).paginate(page=int(page_num), per_page=int(page_size), error_out=False)
    exceptions_list = []
    for i in page_exception.items:
        exceptions_list.append({
            "time": i.time,
            "dorm": i.address,
            "type": i.type,
            "video": i.video
        })
    response_consume_dic = {
        "data": {
            "exceptions": exceptions_list,
            "total": total
        },
        "meta": {
            "msg": "登录成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)

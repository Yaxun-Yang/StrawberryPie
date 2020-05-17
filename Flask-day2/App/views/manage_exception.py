
from flask import Blueprint, request, jsonify, Response
from ..models import Warn
from App.views.first import user
exception = Blueprint('exception', __name__)
video_name = ''


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
            "id": i.id,
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


@exception.route("/api/exception_video", methods=['GET'])
def get_video_time():
    video_id = request.args.get('id')
    get_video = Warn.query.filter_by(id=video_id).first()
    print(get_video.video)
    global video_name
    video_name = get_video.video
    return "ff"

@exception.route("/api/exception/video")
def get_exception_video():
    # 查看历史视频App/static/VID_20200429_152207.mp4E:\Python Program\Flask-day2\App\static\VID_20200429_161822.mp4
    # 根据存放路径修改
    base_path = "E:\\Python Program\\Flask-day2\\App\\static\\"
    global video_name
    print("now"+video_name)
    with open(base_path + video_name, 'rb') as video_file:
        video_history = video_file.read()
        # print(video_history)
    video_file.close
    response_consume_dic = {
        "data": {
            "video": video_history
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        }
    }
    # 变换类型需修改
    return Response(video_history, content_type='video/mp4')

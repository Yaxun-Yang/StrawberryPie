from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from ..models import Historyvideo
from App.ext import db
from App.views.first import user
video = Blueprint('video', __name__)
video_name = ''


@video.route("/api/video/now", methods=['GET'])
def get_video_now():
    #查看实时视频
    response_consume_dic = {
        "meta": {
            "msg": "获取成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)


@video.route("/api/video/history", methods=['GET'])
def get_video_history():
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


@video.route("/api/video/time", methods=['GET'])
def get_video_time():
    video_id = request.args.get('id')
    get_video = Historyvideo.query.filter_by(id=video_id).first()
    print(get_video.video)
    global video_name
    video_name = get_video.video
    return "ff"


@video.route("/api/video/history/information", methods=['GET'])
def get_video_history_information():
    roomnum = user.roomnum
    query = request.args.get('query')
    page_num = request.args.get('pagenum')
    page_size = request.args.get('pagesize')
    exception_data = Historyvideo.query.filter(Historyvideo.roomnum.contains(roomnum)).all()
    total = len(exception_data)
    video_information = []
    page_video_information = Historyvideo.query.filter(Historyvideo.roomnum.contains(roomnum)).paginate(page=int(page_num), per_page=int(page_size), error_out=False)
    for i in page_video_information.items:
        if i.type == 1:
            i.type = "正常"
        else:
            i.type = "异常"
        video_information.append({
            "id": i.id,
            "time": i.time,
            "type": i.type,
            "video": i.video
        })
    response_consume_dic = {
        "data": {
            "information": video_information
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        },
        "total": total
    }
    return response_consume_dic

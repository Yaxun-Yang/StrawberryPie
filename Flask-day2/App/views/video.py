from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify

from .test import VideoCamera
from ..models import Historyvideo, Information
from App.ext import db
# from App.views.first import user
from .first import userList
from App.token.authorization_token import authorization_token
from ..requestuser import User

video = Blueprint('video', __name__)
video_name = ''


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@video.route("/api/video/now", methods=['GET'])
def get_video_now():
    user_token = request.headers.get("Authorization")
    # print(user_token)
    user = authorization_token(userList, user_token)
    if user is None:
        print("show")
        # 查看实时视频
        return Response(gen(VideoCamera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
        # response_consume_dic = {
        #     "meta": {
        #         "msg": "获取成功",
        #         "status": 200
        #     }
        # }
        # return jsonify(response_consume_dic)


@video.route("/api/video/history", methods=['GET'])
def get_video_history():
    # 查看历史视频App/static/VID_20200429_152207.mp4E:\Python Program\Flask-day2\App\static\VID_20200429_161822.mp4
    # 根据存放路径修改
    # 如果开启前端 将下面两行代码放出来 把上面一行代码注释
    # user_token = request.headers.get("Authorization")
    # user = authorization_token(userList, user_token)
    # 如果不开启前端 把上面两行代码注释 放出下面一行
    user = User('李梦瑶', '新二舍102', 'fffffff')
    user_information = Information.query.filter_by(username=user.username).first()
    phone_num = user_information.phone_num
    room_number = user_information.roomnumber
    username = user_information.username
    if user is not None:
        global video_name
        print("now"+video_name)
        path = "./App/static/"
        # with open(base_path + video_name, 'rb') as video_file:
        with open(path + video_name, 'rb') as video_file:
            video_history = video_file.read()
            # print(video_history)
        video_file.close
        # 变换类型需修改
        return Response(video_history, content_type='video/mp4')


@video.route("/api/video/time", methods=['GET'])
def get_video_time():
    user_token = request.headers.get("Authorization")
    # print(user_token)
    user = authorization_token(userList, user_token)
    if user is not None:
        video_id = request.args.get('id')
        get_video = Historyvideo.query.filter_by(id=video_id).first()
        print(get_video.video)
        global video_name
        video_name = get_video.video
        return "ff"


@video.route("/api/video/history/information", methods=['GET'])
def get_video_history_information():
    user_token = request.headers.get("Authorization")
    user = authorization_token(userList, user_token)
    if user is not None:
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




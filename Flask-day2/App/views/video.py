from flask import Blueprint, request, render_template, make_response, abort, Response, session, jsonify
from ..models import Information, Consumption, Environment, Plant, Login, Admin, Bedroom, Rules
from App.ext import db
from App.views.first import user
video = Blueprint('video', __name__)


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
    # 查看历史视频
    response_consume_dic = {
        "meta": {
            "msg": "获取成功",
            "status": 200
        }
    }
    return jsonify(response_consume_dic)

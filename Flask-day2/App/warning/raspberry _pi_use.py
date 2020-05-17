from App.models import Information
from App.views.first import user
from App.warning.receive import insert_warn, update_dorm_condition


def catch_warn():
    # 定义 insert_warn 函数中的参数
    # user保留登陆用户的 username, classnum, token
    address = user.roomnum
    # retype有 宿舍门未关 有人闯入 宿舍某些电器（主要是空调）异常等
    retype = ''
    # 发现异常时间 YYYY-MMMM-DDDD hh:mm:ss 格式（DATETIME类型）
    time = ''
    # 填写video地址
    video = ''
    # 定义 update_dorm_condition 函数中的参数
    # user保留登陆用户的 username, classnum, token
    address = user.roomnum
    # warn_type 有三个取值 分别是 door aircondition invasion 分别代表 门 空调 有人闯入
    warn_type = ''
    # warn_status有两个取值 0，1 分别表示 无异常和有异常
    warn_status = 1
    insert_warn(address, retype, time, video)
    update_dorm_condition(address, warn_type, warn_status)

    # 向用户发送短信提醒 只针对 空调问题和有人闯入
    # 这里需要发短信通知用户 已列出 电话，用户名，宿舍号信息
    information = Information.query.filter_by(username=user.username).first()
    phone_number = information.phonenum
    student_name = information.username
    student_roomnumber = information.roomnumber


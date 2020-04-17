from App.ext import db
from App.models import Warn, Dormcondition


def insert_warn(address, re_type, time, video):
    receive_w = Warn
    receive_w.address = address
    receive_w.type = re_type
    receive_w.time = time
    receive_w.video = video
    db.session.add(receive_w)
    db.session.commit()


def update_dorm_condition(address, warn_type, warn_status):
    dorm_condition = Dormcondition.query.filter(Dormcondition.address.contains(address)).first()
    if warn_type == 'door':
        dorm_condition.door = warn_status
    elif warn_type == 'aircondition':
        dorm_condition.aircondition = warn_status
    elif warn_type == 'invasion':
        dorm_condition.invasion = warn_status
    db.session.commit()

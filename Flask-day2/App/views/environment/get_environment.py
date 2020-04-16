from App.models import Environment
from App.ext import db
from .get_environment_condition import get_information
import time


def insert_environment():
    weather_list = get_information()
    weather = weather_list[len(weather_list)-1]
    print(weather)
    weather['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    environment = Environment(weather['od22'], '23', weather['od27'], '90', weather['time'])
    db.session.add(environment)
    db.session.commit()

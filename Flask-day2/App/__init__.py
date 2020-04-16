from flask import Flask

from App.ext import init_ext
from App.views.first import blue
from App.views.plant import resplant
from App.views.pet import pet
from App.views.room import room
from App.views.admin_lamp import admin_lamp
from App.views.admin_students_information import students


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    app.register_blueprint(resplant)
    app.register_blueprint(pet)
    app.register_blueprint(room)
    app.register_blueprint(admin_lamp)
    app.register_blueprint(students)
    init_ext(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/hello"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'jjj'
    return app

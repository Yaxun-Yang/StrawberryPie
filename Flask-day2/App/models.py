from App.ext import db


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    authetic = db.Column(db.Integer)
    name = db.Column(db.String(45))


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    adminid = db.Column(db.String(45))
    type = db.Column(db.String(45))
    dept = db.Column(db.String(45))
    building = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    room = db.Column(db.Integer)
    people = db.Column(db.Integer)
    address = db.Column(db.String(45))


class Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    classnum = db.Column(db.String(45))
    roomnumber = db.Column(db.String(45))
    roommate = db.Column(db.String(45))
    img = db.Column(db.String(45))
    college = db.Column(db.String(45))
    stuid = db.Column(db.String(45))
    stutype = db.Column(db.String(45))
    time = db.Column(db.String(45))
    phonenum = db.Column(db.String(45))


class Consumption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    water = db.Column(db.String(45))
    electricity = db.Column(db.String(45))
    date = db.Column(db.Date)
    roomnum = db.Column(db.String(45))


class Environment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indoortem = db.Column(db.String(45))
    outdoortem = db.Column(db.String(45))
    indoorhum = db.Column(db.String(45))
    outdoorhum = db.Column(db.String(45))
    time = db.Column(db.DATETIME(2))

    def __init__(self, indoortem, outdoortem, indoorhum, outdoorhum, time):
        self.indoortem = indoortem
        self.outdoortem = outdoortem
        self.indoorhum = indoorhum
        self.outdoorhum = outdoorhum
        self.time = time


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String(45))
    plantname = db.Column(db.String(45))
    imgurl = db.Column(db.String(45))
    percent = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    watertime = db.Column(db.String(45))


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String(45))
    petname = db.Column(db.String(45))
    imgurl = db.Column(db.String(45))
    percent = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    feedtime = db.Column(db.String(45))


class Bedroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String(45))
    devnum = db.Column(db.Integer())
    opentime = db.Column(db.String(45))
    doorcon = db.Column(db.Integer)
    lamplight = db.Column(db.String(45))
    lampcon = db.Column(db.Integer)
    airconditiontem = db.Column(db.String(45))
    airconditioncon = db.Column(db.Integer)
    watertemp = db.Column(db.String(45))
    watercon = db.Column(db.Integer)


class Toilet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String(45))
    devnum = db.Column(db.Integer())
    lamplight = db.Column(db.String(45))
    lampcon = db.Column(db.Integer)


class Balcony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String(45))
    devnum = db.Column(db.Integer())
    lamplight = db.Column(db.String(45))
    lampcon = db.Column(db.Integer)


class Rules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String(45))
    lampclosetime = db.Column(db.Integer())
    lampremindtime = db.Column(db.String(45))



from flask_cors import CORS
# from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App import create_app
from App.models import db

app = create_app()
CORS(app, resources=r'/*')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


#app的errorhandler和blue的handler的区别 app的可以捕获全局的错误
@app.errorhandler(404)
def handler(error):
    return '404'


if __name__ == '__main__':
    manager.run()

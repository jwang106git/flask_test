#to run === 1 === python manage.py shell
#to run === 1 === python manage.py server

from flask_script import Server,Manager
from main import app

manager = Manager(app)
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    return dict(app=app)
if __name__ == "__main__":
    manager.run()


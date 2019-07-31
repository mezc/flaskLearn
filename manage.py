from flask_script import Manager
from app import app
from modules import User
manager = Manager(app)

@manager.command
def save():
  # user = User('jike', 'jike@jikexueyuan.com')
  # user.save()
  user = User(name="jike", email="jike@com")
  user.save()

@manager.command
def query_users():
  # users = User.query_users()
  users = User.objects.all()
  for user in users:
    print(user)

if __name__ == "__main__":
  manager.run()
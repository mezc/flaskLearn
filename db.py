import pymysql

db = pymysql.connect('localhost', 'root', '666666', 'test')

cursor = db.cursor()

def addUser(username, password):
  sql = "insert into userInfo (username, password) values ('{}','{}')".format(username, password)
  cursor.execute(sql)
  db.commit()
  cursor.close()
  db.close()
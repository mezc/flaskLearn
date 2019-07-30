import pymysql
# connect
db = pymysql.connect("localhost", "root", "666666", "test")
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
# cursor = db.cursor()
while True:
  name = input("please input:")
  sql = "select * from students"
  # insert_sql = "insert into students (name) values ('wanger')"
  insert_sql = "insert into students (name) values ('{}')".format(name)
  cursor.execute(insert_sql)

  db.commit()

  cursor.execute(sql)

  # cursor.close()
  # db.close()
  data = cursor.fetchall()
  print(data)
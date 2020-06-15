# coding=utf-8

import sqlite3

# 连接一个数据库，没有的话会自动创建
conn = sqlite3.connect('../dianping.db')
print("Opened database successfully")
# 创建一个游标
c = conn.cursor()

# 往表里面插入数据
# c.execute("INSERT INTO article ('content') VALUES ('22asdad打算打算'),  ('11asdad打算打算') ")
sql_values = 'INSERT INTO article VALUES '
datas="111aavas"
# sql = "Insert Into p ({1}) Values('张三', '语文', '90')".format(table_name, fields_name)
# sql_values = "Insert Into p Values(\"\"\"{1}\"\"\")".format(datas)
sql_values = "Insert Into p Values({0})".format(datas)
print(sql_values)
c.execute(sql_values)

cursor = c.execute(sql_values)
conn.commit()
conn.close()

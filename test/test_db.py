# coding=utf-8

import sqlite3

# 连接一个数据库，没有的话会自动创建
conn = sqlite3.connect('../dianping.db')
print("Opened database successfully")
# 创建一个游标
c = conn.cursor()
# 创建一张表
# c.execute('''CREATE TABLE content
#        (id INT PRIMARY KEY   NOT NULL,
#        name           TEXT    ,
#        word            TEXT)  ''')
# print("Table created successfully")

# 往表里面插入数据
# c.execute("INSERT INTO article ('content') VALUES ('22asdad打算打算'),  ('11asdad打算打算') ")
sql_values = 'INSERT INTO article VALUES '
datas= [("aavas"),("aas87111")]
for i in range(0, len(datas)):  # 列表下标索引，一一提取一行数据
    sql_values += '('  # 增加execute语句所需的左括号
    sql_values += datas[i] # 插入数据
    sql_values += '),'  # 右括号
sql_values = sql_values.strip(',')  # 去除最后一行数据的逗号，也可replace为分号
sql_values = """INSERT INTO article (content) VALUES (aavas),(aas87111)"""
print(sql_values)
c.execute(sql_values)

# for i in range(1):
#     sql
# c.execute(sql, data)

# # 删除表里面的数据
# c.execute("DELETE FROM content WHERE id=2")
# # 更改表里面的数据
# c.execute("UPDATE content SET  id=4  WHERE id=3")
# 查询表里面的数据
cursor = c.execute("SELECT content from article")
for row in cursor:
    print("content = ", row[0])
conn.commit()
conn.close()

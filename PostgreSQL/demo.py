# 导入依赖包
# !/usr/bin/python3

import psycopg2

print("running");


# 创建连接对象
conn = psycopg2.connect(database="Test", user="postgres", password="admin", host="localhost", port="5432")
cur = conn.cursor()  # 创建指针对象
print("connected successfully")
# 创建表
cur.execute("CREATE TABLE student(id integer,name varchar,sex varchar);")

# 插入数据
cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s);", (1, 'Aspirin', 'M'))
cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s);", (2, 'Taxol', 'F'))
cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s);", (3, 'Dixheral', 'M'))
conn.commit()

# 获取结果
cur.execute('SELECT * FROM student;')
results = cur.fetchall()
print(results)

# 关闭练级
cur.close()
conn.close()
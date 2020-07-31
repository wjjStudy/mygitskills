import pymysql

# 1. 建立连接
conn = pymysql.connect(host='10.111.32.82',
                       port=10208,
                       user='root',
                       passwd='2019IVAmysqlP@ssword',   # password也可以
                       db='senseface',
                       charset='utf8')   # 如果查询有中文需要指定数据库编码

# 2. 从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

# 3. 查询数据库（读）
cur.execute("select * from info_video_resource_async ")

# 4. 获取查询结果
result = cur.fetchall()
print(result)

# 3. 更改数据库（写）
# cur.execute("delete from user where name='李四'")

# 4. 提交更改
# conn.commit()  # 注意是用的conn不是cur

# 5. 关闭游标及连接
cur.close()
conn.close()

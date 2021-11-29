# -*- coding: utf-8 -*-




import pymysql
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='推荐系统')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select id,username from user where username=%s and password=%s",['长江以北吴彦祖','1234'])
obj=cursor.fetchone()
conn.commit()
cursor.close()
conn.close()
print(obj)


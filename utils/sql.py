import pymysql
class SQLHelper(object):
    @staticmethod
    def open():
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='推荐系统')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn,cursor

    @staticmethod
    def close(conn,cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def fetch_one(sql,args):

        conn,cursor = SQLHelper.open()
        #cursor.execute("select id,username from user where username=%s and password=%s", ['长江以北吴彦祖', '1234'])
        cursor.execute(sql, args)
        obj = cursor.fetchone()
        SQLHelper.close(conn,cursor)
        return obj

    @staticmethod
    def fetch_all(sql):
        conn,cursor = SQLHelper.open()
        # cursor.execute("select id,username from user where username=%s and password=%s", ['长江以北吴彦祖', '1234'])
        cursor.execute(sql)
        obj = cursor.fetchall()
        SQLHelper.close(conn,cursor)
        return obj

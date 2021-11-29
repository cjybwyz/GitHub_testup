import random

from flask import Flask, request, render_template, session, flash, redirect, url_for
from utils.sql import  SQLHelper
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='secret_key'
#连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/3306/推荐系统'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
#     name = db.Column(db.String(20), nullable=False)
#     password = db.Column(db.String(30), nullable=False)
#     def __repr__(self):
#         return 'User:%s'%self.name
# db.create_all()
list0 = []
list22=[]
list_hot = []
@app.route('/')
def index_view():
    sss1 = range(1, 151)
    A = random.sample(sss1, 7)
    print(A)

    for I in range(0, len(A)):
        obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                   [int(A[I]), ])
        list0.append(obj3)
    print(list0)
    obj0 = SQLHelper.fetch_all('select action from user2  ')
    print(obj0)
    a = obj0
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    for i in a:
        list7.append(i['action'].split(","))
    for i in list7:
        for j in i:
            list8.append(int(j))
    for i in list8:
        if i not in list9:
            list9.append(int(i))
    for i in list9:
        a = list8.count(i)
        list10.append(a)

    list_lable1 = [[0 for i in range(10)] for j in range(3)]
    dict1 = {}
    list_lable2 = [[0 for i in range(10)] for j in range(3)]
    dict2 = {}
    list_lable3 = [[0 for i in range(10)] for j in range(3)]
    dict3 = {}
    list_lable4 = [[0 for i in range(10)] for j in range(3)]
    dict4 = {}
    list_lable5 = [[0 for i in range(10)] for j in range(3)]
    dict5 = {}
    for i in list9:
        if i < 64:
            list_lable1[0].append(i)
            flag = list9.index(i)
            list_lable1[1].append(list10[flag])
        if i >= 64 and i <= 83:
            list_lable2[0].append(i)
            flag = list9.index(i)
            list_lable2[1].append(list10[flag])
        if i >= 84 and i <= 103:
            list_lable3[0].append(i)
            flag = list9.index(i)
            list_lable3[1].append(list10[flag])
        if i >= 104 and i <= 123:
            list_lable4[0].append(i)
            flag = list9.index(i)
            list_lable4[1].append(list10[flag])
        if i >= 124 and i <= 151:
            list_lable5[0].append(i)
            flag = list9.index(i)
            list_lable5[1].append(list10[flag])
    list_dict = []
    for i in range(0, len(list_lable1[0])):
        dict1[list_lable1[0][i]] = list_lable1[1][i]
    for i in range(0, len(list_lable2[0])):
        dict2[list_lable2[0][i]] = list_lable2[1][i]
    for i in range(0, len(list_lable3[0])):
        dict3[list_lable3[0][i]] = list_lable3[1][i]
    for i in range(0, len(list_lable4[0])):
        dict4[list_lable4[0][i]] = list_lable4[1][i]
    for i in range(0, len(list_lable5[0])):
        dict5[list_lable5[0][i]] = list_lable5[1][i]
    list_dict.append(dict1)
    list_dict.append(dict2)
    list_dict.append(dict3)
    list_dict.append(dict4)
    list_dict.append(dict5)
    list_hot = []

    for i in list_dict:
        list_1 = list(i.items())
        my_dict_sortbyvalue = dict(sorted(list_1, key=lambda x: x[1]))
        x = my_dict_sortbyvalue.popitem()
        list_hot.append(x[0])
        x = my_dict_sortbyvalue.popitem()
        list_hot.append(x[0])
    print(list_hot)
    list_b = []
    for I in range(0, len(list_hot)):
        obj_hot = SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                                      [int(list_hot[I]), ])
        list_b.append(obj_hot)
    print(list_b)
    return render_template('index.html',list2=list0,list_b=list_b)

@app.route('/clicked',methods=['POST','GET'])
def clicked():
    list=[]
    if list0[0]['id']<'64':
        sss1=range(1,63)
        A=random.sample(sss1,6)
        for I in range(0, len(A)):
            obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                       [int(A[I]), ])
            list.append(obj3)
            #科技
    elif list0[0]['id']<'84':
        sss1 = range(1, 83)
        A = random.sample(sss1, 6)
        for I in range(0, len(A)):
            obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                       [int(A[I]), ])
            list.append(obj3)
            #国际
    elif list0[0]['id']<'104':
        sss1 = range(1, 103)
        A = random.sample(sss1, 6)
        for I in range(0, len(A)):
            obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                       [int(A[I]), ])
            list.append(obj3)
            #法治
    elif list0[0]['id']<'124':
        sss1 = range(1, 123)
        A = random.sample(sss1, 6)
        for I in range(0, len(A)):
            obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                       [int(A[I]), ])
            list.append(obj3)
            #军事
    elif list0[0]['id']<'152':
        sss1 = range(1, 151)
        A = random.sample(sss1, 6)
        for I in range(0, len(A)):
            obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                       [int(A[I]), ])
            list.append(obj3)
    print(list)
    return render_template('clicked.html',list2=list0,list3=list)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    name = request.form.get('name')
    password = request.form.get('password')
    obj=SQLHelper.fetch_one('select id,username from user where username=%s and password=%s',[name,password, ])
    if obj:
        session.permanent=True
        session['user_info']={'id':obj['id'],'name':name}
        return redirect('/index')
    else:
        return render_template('login.html',msg='用户名或密码错误')

@app.route('/index',methods=['POST','GET'])
def index():
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    list2 = []
    obj0=SQLHelper.fetch_all('select action from user2  ')
    print(obj0)
    for i in obj0:
        list2.append(i['action'].split(','))

    print(session['user_info']['name'])
    obj = SQLHelper.fetch_one('select name,action from user2 where name=%s ', [session['user_info']['name'], ])
    print(obj)

    #用户行为数据分析
    list_a = str(obj['action']).split(",")
    print(list_a)
    for i in range(0,len(list_a)):
        obj2 = SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                              [int(list_a[i]), ])
        if obj2['lable']=='红色故事':
            s1+=1
        elif obj2['lable']=='科技':
            s2+=1
        elif obj2['lable']=='国际':
            s3+=1
        elif obj2['lable']=='军事':
            s4+=1
        elif obj2['lable']=='法治':
            s5+=1
        print(obj2)
    S1=7*s1/(s1+s2+s3+s4+s5)
    S2=7*s2/(s1+s2+s3+s4+s5)
    S3 = 7 * s3 / (s1 + s2 + s3 + s4 + s5)
    S4 = 7 * s4 / (s1 + s2 + s3 + s4 + s5)
    S5 = 7 * s5 / (s1 + s2 + s3 + s4 + s5)
    if S1%1>0.5:
        ss1=int(S1)+1
    else:
        ss1=int(S1)
    if S2%1>0.5:
        ss2=int(S2)+1
    else:
        ss2=int(S2)
    if S3%1>0.5:
        ss3=int(S3)+1
    else:
        ss3=int(S3)
    if S4%1>0.5:
        ss4=int(S4)+1
    else:
        ss4=int(S4)
    if S5%1>0.5:
        ss5=int(S5)+1
    else:
        ss5=int(S5)
    print(ss1,ss2,ss3,ss4,ss5)
    #判断红色故事新闻推荐数量
    sss1=range(1, 63)
    A= random.sample(sss1,ss1)
    print(A)

    for I in range(0,len(A)):
        obj3=SQLHelper.fetch_one('select id,title,brief,img_src,lable ,message from article where id=%s ',
                              [int(A[I]), ])
        list22.append(obj3)
    print(list22)
    #判断科技新闻推荐数量
    sss2 = range(64, 83)
    B = random.sample(sss2, ss2)
    print(B)
    list3 = []
    for I in range(0, len(B)):
        obj4 = SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                                   [int(B[I]), ])
        list3.append(obj4)
    print(list3)
    #判断国际新闻推荐数量
    sss3 = range(84, 103)
    C = random.sample(sss3, ss3)
    print(C)
    list4 = []
    for I in range(0, len(C)):
        obj5 = SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                                   [int(C[I]), ])
        list4.append(obj5)
    print(list4)
    #判断军事新闻推荐数量
    sss4 = range(104, 123)
    D = random.sample(sss4, ss4)
    print(D)
    list5 = []
    for I in range(0, len(D)):
        obj6 = SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                                   [int(D[I]), ])
        list5.append(obj6)
    print(list5)
    #判断法治新闻推荐数量
    sss5 = range(124, 151)
    E = random.sample(sss5, ss5)
    print(E)
    list6 = []
    for I in range(0, len(E)):
        obj7 = SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                                   [int(E[I]), ])
        list6.append(obj7)
    print(list6)

    #热点判断
    a=obj0
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    for i in a:
        list7.append(i['action'].split(","))
    for i in list7:
        for j in i:
            list8.append(int(j))
    for i in list8:
        if i not in list9:
            list9.append(int(i))
    for i in list9:
        a = list8.count(i)
        list10.append(a)

    list_lable1 = [[0 for i in range(10)] for j in range(3)]
    dict1 = {}
    list_lable2 = [[0 for i in range(10)] for j in range(3)]
    dict2 = {}
    list_lable3 = [[0 for i in range(10)] for j in range(3)]
    dict3 = {}
    list_lable4 = [[0 for i in range(10)] for j in range(3)]
    dict4 = {}
    list_lable5 = [[0 for i in range(10)] for j in range(3)]
    dict5 = {}
    for i in list9:
        if i < 64:
            list_lable1[0].append(i)
            flag = list9.index(i)
            list_lable1[1].append(list10[flag])
        if i >= 64 and i <= 83:
            list_lable2[0].append(i)
            flag = list9.index(i)
            list_lable2[1].append(list10[flag])
        if i >= 84 and i <= 103:
            list_lable3[0].append(i)
            flag = list9.index(i)
            list_lable3[1].append(list10[flag])
        if i >= 104 and i <= 123:
            list_lable4[0].append(i)
            flag = list9.index(i)
            list_lable4[1].append(list10[flag])
        if i >= 124 and i <= 151:
            list_lable5[0].append(i)
            flag = list9.index(i)
            list_lable5[1].append(list10[flag])
    list_dict = []
    for i in range(0, len(list_lable1[0])):
        dict1[list_lable1[0][i]] = list_lable1[1][i]
    for i in range(0, len(list_lable2[0])):
        dict2[list_lable2[0][i]] = list_lable2[1][i]
    for i in range(0, len(list_lable3[0])):
        dict3[list_lable3[0][i]] = list_lable3[1][i]
    for i in range(0, len(list_lable4[0])):
        dict4[list_lable4[0][i]] = list_lable4[1][i]
    for i in range(0, len(list_lable5[0])):
        dict5[list_lable5[0][i]] = list_lable5[1][i]
    list_dict.append(dict1)
    list_dict.append(dict2)
    list_dict.append(dict3)
    list_dict.append(dict4)
    list_dict.append(dict5)


    for i in list_dict:
        list_1 = list(i.items())
        my_dict_sortbyvalue = dict(sorted(list_1, key=lambda x: x[1]))
        x = my_dict_sortbyvalue.popitem()
        list_hot.append(x[0])
        x = my_dict_sortbyvalue.popitem()
        list_hot.append(x[0])
    print(list_hot)
    list_b = []
    for I in range(0, len(list_hot)):
        obj_hot=SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                                   [int(list_hot[I]), ])
        list_b.append(obj_hot)
    print(list_b)
    list_readed=[]
    obj_readed=SQLHelper.fetch_one('select action from user2 where name=%s ',
                                   [session['user_info']['name'], ])
    list_readed = obj_readed['action'].split(',')
    print(list_readed)
    list_read=[]
    for W in range(0,len(list_readed)):
        obj_read=SQLHelper.fetch_one('select id,title,brief,img_src,lable from article where id=%s ',
                                   [int(list_readed[W]), ])
        list_read.append(obj_read)
    print(list_read)
    return render_template('indexed.html',list_read=list_read,list2=list22,list3=list3,list4=list4,list5=list5,list6=list6,list_b=list_b)


@app.route('/clicked2', methods=['POST', 'GET'])
def clicked2():
    sss1 = range(1, 63)
    list23=[]
    A = random.sample(sss1, 6)
    print(A)

    for I in range(0, len(A)):
        obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                   [int(A[I]), ])
        list23.append(obj3)
    print(list23)
    print(list22[0]['message'])
    return render_template('clicked2.html',list2=list22,list3=list23)



@app.route('/clicked3',methods=['POST','GET'])
def clicked3():
    sss1 = range(64, 83)
    list23 = []
    A = random.sample(sss1, 6)
    print(A)

    for I in range(0, len(A)):
        obj3 = SQLHelper.fetch_one('select id,title,brief,img_src,lable ,message from article where id=%s ',
                                   [int(A[I]), ])
        list23.append(obj3)
    print(list_hot)
    list24=[]
    for i in range(0, len(list_hot)):
        obj4 = SQLHelper.fetch_one('select id,title,brief,img_src,lable,message from article where id=%s ',
                                   [int(list_hot[i]), ])
        list24.append(obj4)
    print(list24)
    return render_template('clicked3.html' ,list2=list24,list3=list23)

@app.route('/register',methods=['POST','GET'])
def register():
    return render_template('register.html')

@app.route('/search',methods=['POST','GET'])
def searchout():
    file = request.form.get('search')
    print(file)



    return render_template('searchout.html')


if __name__ == '__main__':
    app.run()

import MySQLdb
db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='lyf1995123',port=3306)
cur=db.cursor()
cur.execute('select version()')
data=cur.fetchone()
print "Database Version : %s " %data
#数据库插入操作
cur.execute('use test')
cur.execute('show create table dorm')
data=cur.fetchall()
print(data)
sql="""insert into dorm (studentid,name,phone,QQ)values ('201422010400x','yyj','13000000000','777777777')"""
try:
    cur.execute(sql)
    cur.execute('select*from dorm ordered by studentid')
    data=cur.fetchall()
    print(data)
    db.commit()
except:
    print("数据库插入操作失败")
    db.rollback()
finally:
    db.close()
 

       

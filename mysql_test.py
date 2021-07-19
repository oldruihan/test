import pymysql    #导入模块
conn = pymysql.connect(host='127.0.0.1', user='root', password="root",database ='btest')
# host=localhost #也可以写,如果127.0.0.1不能用的话#  登录数据库
cur = conn.cursor()   # 数据库操作符 游标
cur.execute('insert into user(username,password) values ("hans","12222")')
#()里填 sql 语句 注意'sql语句中的""引号要与最外为的引号区分开w'
conn.commit()  #提交数据
cur.close()    #关闭游标
conn.close()   #断开数据库,释放资源
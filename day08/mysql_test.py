# @Time : 2019/5/8 10:32
# @Author : 2273360936@qq.com
# @FileName : mysql_test.py
# @GitHub : https://github.com/liulichao1/python-0426
import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='chao0309@'
)
cursor = connection.cursor()

cursor.execute('drop database if exists db_python')

cursor.execute('create database db_python ')

cursor.execute('show databases')

for db in cursor:
    print(db)

cursor.execute('drop table if exists db_python.user')

sql = """
create table db_python.user(
id int auto_increment primary key comment 'id PK',
email varchar(255) not null unique comment 'email NN UN',
password varchar(255) not null comment 'password NN'
 )comment 'user table';                         
"""
cursor.execute(sql)

cursor.execute('drop table if exists db_python.book')

sql = """
create table db_python.book(
id int auto_increment primary key comment 'id PK',
title varchar(255) not null unique comment 'title NN UN',
author varchar(255) not null comment 'author NN',
userId int comment 'user id FK'
 )comment 'book table';  
"""
cursor.execute(sql)

cursor.execute("""
alter table db_python.book
add constraint book_fk_userId
foreign key (userId)
references db_python.user(id)
""")

cursor.execute('show tables from db_python')

for table in cursor:
    print(table)

cursor.execute("""
insert into db_python.user(email, password) 
value ('tom@tom.com','123'),('jerry@jerry.com','abc')
""")

sql = 'insert into db_python.user(email, password) value (%s,%s)'
val = ('spike@spike.com', '456')

cursor.execute(sql, val)

connection.commit()

cursor.execute('''
insert into db_python.book(title, author, userId)
values
('HTML','author-1', 1),
('CSS','author-2', 2),
('JavaScript','author-3', 2),
('MyBatis','author-4', 3),
('Spring','author-5', 3),
('Python 编程基础','author-6', 3)
''')
# print(cursor.rowcount)
#
connection.commit()

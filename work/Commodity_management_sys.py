# @Time : 2019/5/9 10:28
# @Author : 2273360936@qq.com
# @FileName : Commodity_management_sys.py
# @GitHub : https://github.com/liulichao1/python-0426
import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='chao0309@'
)

cursor = conn.cursor()

cursor.execute('drop database if exists  db_commodity')

cursor.execute('create database db_commodity')
cursor.execute('show databases')

for db in cursor:
    print(db)

cursor.execute('drop table if exists db_commodity.commodity')

sql = """
create table db_commodity.commodity(
id int auto_increment primary key comment 'id PK',
number varchar(255) not null unique comment 'num NN UN',
name varchar(255) not null comment 'name NN',
price float not null comment 'price NN',
amount int comment 'amount '

 )comment 'commodity table';                         
"""
cursor.execute(sql)

cursor.execute('show tables from db_commodity')
for table in cursor:
    print(table)

cursor.execute("""
insert into db_commodity.commodity( number, name, price, amount) 
values ('1434352324','空调','3400.5',100)   ,
       ('1434352325','洗衣机','2300.6',200),
       ('1434352326','电脑','6000',500),
       ('1434352327','电视','4400',300)

""")
conn.commit()
cursor.execute("""
select * from db_commodity.commodity  where name = '空调'

""")
values = cursor.fetchall()  # 接收全部的返回结果行
print(values)

cursor.execute("""
update

""")

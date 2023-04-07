import mysql.connector
from mysql.connector import Error
import os
from configparser import ConfigParser
from prettytable import PrettyTable

def connect():    
    config=ConfigParser()
    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#abspath main.py的絕對位置
    config.read(os.path.join(parent_parent_dir,"database.config.ini"))

    ## /database_config.ini
    # [database]
    # host=localhost
    # port=3306
    # username=
    # password=
    # database=customer_order    

    db_config={
        'host':config.get('database','host'),
        'port':config.get('database','port'),
        'user':config.get('database','username'),
        'password':config.get('database','password'),
        'database':config.get('database','database'),
        # 'auth_plugin':'caching_sha2_password'# 在 MySQL 8.0 版本中，預設身份驗證已經變更為 caching_sha2_password
    }

    try:
        conn=mysql.connector.connect(**db_config) # **db_config是字典 
        return conn       
    except Error as e:
        print(e)

def sqlData(conn=None,sql="select customers.name,customers.email,orders.order_date,orders.total from customers,orders where customers.customer_id=orders.customer_id;"):
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    table=PrettyTable()
    
    # 表格的欄位名稱
    table.field_names = [i[0] for i in cur.description]
    
    # 將資料加入表格
    for row in result:
        table.add_row(row)
    print(table)


if __name__ == "__main__":
    conn=connect()
    # print(conn.is_connected())
    sql=input('sql指令(預設輸出兩表合併)')
    if(sql):
        sqlData(conn,sql)
    else:
        sqlData(conn)

    conn.close()


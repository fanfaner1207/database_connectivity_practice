from configparser import ConfigParser
import mysql.connector
from mysql.connector import Error

def connect():
    config=ConfigParser()
    config.read("../database.config.ini")

    db_config={
        'host':config.get('database','host'),
        'port':config.get('database','port'),
        'user':config.get('database','username'),
        'password':config.get('database','password'),
        'database':config.get('database','database'),
        'auth_plugin':'cashing_sha2_password'# 在 MySQL 8.0 版本中，預設身份驗證已經變更為 caching_sha2_password
    }

    try:
        with mysql.connector.connect(**db_config) as conn:
            print('1')
    except Error as e:
        print(e)


if __name__ == "__main__":
    connect()
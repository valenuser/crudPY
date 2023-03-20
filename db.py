import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def showDB():
    conn = pymysql.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password')
    )

    cursor = conn.cursor()

    sql = 'SHOW DATABASES'

    cursor.execute(sql)

    return cursor.fetchall()


def createDB(nameDB):
    conn = pymysql.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password')
    )

    cursor = conn.cursor()
    sql = 'create database '+nameDB+''
    cursor.execute(sql)
    conn.commit()
    conn.close()



def deleteDB(nameDB):
    conn = pymysql.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password')
    )

    cursor = conn.cursor()

    sql = 'drop database '+nameDB+''

    cursor.execute(sql)

    

def createTable(nameDB,nameTable,nameCampo,tipoDato,signos,incrementable,questionPK):
    conn = pymysql.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database= nameDB
    )

    cursor = conn.cursor
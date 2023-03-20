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

    conn.commit()
    conn.close()

    

def createTable(nameDB,nameTable,nameCampo,tipoDato,signos,incrementable,questionPK):
    conn = pymysql.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database= nameDB
    )

    cursor = conn.cursor()


    if incrementable == ' ' and signos == ' ':
        sql = 'create table '+nameTable+'('+nameCampo+' '+tipoDato+' '+questionPK+')'
    elif incrementable == ' ':
        sql = 'create table '+nameTable+'('+nameCampo+' '+tipoDato+' '+signos+' '+questionPK+')'
    elif signos == ' ':
        sql = 'create table '+nameTable+'('+nameCampo+' '+tipoDato+' '+incrementable+' '+questionPK+')'
    else:
        sql = 'create table '+nameTable+'('+nameCampo+' '+tipoDato+' '+n+''+questionPK+')'

    cursor.execute(sql)

    conn.commit()
    conn.close()


def addCampo(nameDB,nameTable,nameCampo,tipoDato,signos,incrementable,questionPK):
    conn = pymysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=nameDB
    )

    cursor = conn.cursor()

    if questionPK == 'PRIMARY KEY':
        sql = 'alter table'+nameTable+' add column '+nameCampo+' '+tipoDato+' '+signos+' '+incrementable+' '+questionPK+''


    if incrementable == ' ' and signos == ' ':
        sql = 'alter table '+nameTable+' add column '+nameCampo+' '+tipoDato+' '+questionPK+''
    elif incrementable == ' ':
        sql = 'alter table '+nameTable+' add column '+nameCampo+' '+tipoDato+' '+signos+' '+questionPK+''
    elif signos == ' ':
        sql = 'alter table '+nameTable+' add column '+nameCampo+' '+tipoDato+' '+incrementable+' '+questionPK+''

    cursor.execute(sql)

    conn.commit()
    conn.close()
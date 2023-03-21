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
        sql = 'create table '+nameTable+'('+nameCampo+' '+tipoDato+' '+signos+' '+incrementable+' '+questionPK+')'

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


    if incrementable == ' ' and signos == ' ':
        sql = 'alter table '+nameTable+' add column '+nameCampo+' '+tipoDato+' '+questionPK+''
    elif incrementable == ' ':
        sql = 'alter table '+nameTable+' add column '+nameCampo+' '+tipoDato+' '+signos+' '+questionPK+''
    elif signos == ' ':
        sql = 'alter table '+nameTable+' add column '+nameCampo+' '+tipoDato+' '+incrementable+' '+questionPK+''
    else:
        sql = 'alter table '+nameTable+' add column'+nameCampo+' '+tipoDato+' '+signos+' '+incrementable+' '+questionPK+''

    cursor.execute(sql)

    conn.commit()
    conn.close()



def showTable(nameDB):
    conn = pymysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=nameDB
    )

    cursor = conn.cursor()

    sql = 'SHOW TABLES'

    cursor.execute(sql)

    return cursor.fetchall()


def showDataTable(nameDB,nameTable):
    conn = pymysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=nameDB
    )

    cursor = conn.cursor()

    sql = 'SELECT * FROM '+nameTable+''

    cursor.execute(sql)

    return cursor.fetchall()


def showColumns(nameDB,nameTable):
    conn = pymysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=nameDB
    )

    cursor = conn.cursor()

    sql = 'SHOW COLUMNS FROM '+nameTable+''

    cursor.execute(sql)

    return cursor.fetchall()



def updateData(nameDB,nameTable,column,dato,idColumn,idName):
    conn = pymysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=nameDB
    )

    cursor = conn.cursor()

    sql = "update "+nameTable+" set "+column+"='"+dato+"' where "+idName+"= "+idColumn+" "

    cursor.execute(sql)

    conn.commit()
    conn.close()


def showUpdate(nameDB,nameTable,column,idColumn,idName):
    conn = pymysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=nameDB
    )

    cursor = conn.cursor()

    sql = 'select '+column+' from '+nameTable+' where '+idName+'='+idColumn+''

    cursor.execute(sql)

    return cursor.fetchall()
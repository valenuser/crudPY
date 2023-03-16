import pymysql


def createDB(nameDB):
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password="Ruta88790"
    )

    cursor = conn.cursor()
    sql = 'create database '+nameDB+''
    cursor.execute(sql)
    conn.commit()


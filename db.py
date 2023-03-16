import pymysql

def showDB():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Ruta88790"
    )

    cursor = conn.cursor()

    sql = 'SHOW DATABASES'

    cursor.execute(sql)

    return cursor.fetchall()


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




#def createTable():

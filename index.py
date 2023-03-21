from tabulate import tabulate
import time


from db import createDB as create
from db import showDB as show
from db import deleteDB as delete
from db import createTable as addTable
from db import addCampo as newCampos
from db import showTable 
from db import showDataTable
from db import showColumns
from db import updateData
from db import showUpdate


#crear funcion para crear campos

def addCampo(nameDB,nameTable):
        nombreCampo = input('Como quieres que se llame el campo? ')
        dato = input('Que tipo de dato quieres que sea? ')

        if dato != 'int':
            tipoDato = dato +'(60)'
        else:
            tipoDato = dato
        signos = input('Quieres que puedan introducirse signos?(y/n) ')

        while True:
            if signos == 'y' or signos == 'n':
                break
            else:
                print('Solo puedes responder escribiendo "y" para afirmar o "n" para negar')
                signos = input('Quieres que puedan introducirse signos?(y/n) ')

        if signos == 'n':
            signos = 'UNSIGNED'
        else:
            signos = ''


        incrementable = input('Deseas que sea auto incrementable?(y/n) ')

        while True:
            if incrementable == 'y' or incrementable == 'n':
                break
            else:
                print('Solo puedes responder escribiendo "y" para afirmar o "n" para negar')
                incrementable = input('Deseas que sea auto incrementable?(y/n)')

        if incrementable == 'y':
            incrementable = 'AUTO_INCREMENT'
        else:
            incrementable = ''

        questionPK = input('Quieres que sea Primary Key? ')

        while True:
            if questionPK == 'y' or questionPK == 'n':
                break
            else:
                print('Solo puedes responder escriibiendo "y" para afirmar o "n" para negar')
                questionPK = input('Quieres que sea Primary Key? ')    

        if questionPK == 'y':
            questionPK = 'PRIMARY KEY'
        elif questionPK == 'n':
            questionNull = input('Deseas que el dato sea nulo o no nulo?(null/not null)')  
            while True:
                if questionNull == 'null' or questionNull == 'not null':
                    break
                else:
                    print('Solo puedes responder escribiendo "null "o "not null"')
                    questionNull = input('Deseas que el dato sea nulo o no nulo?(null/not null)')     

            if questionNull == 'null':
                questionPK = 'NULL'
            else:
                questionPK = 'NOT NULL'  

        newCampos(nameDB,nameTable,nombreCampo,tipoDato,signos,incrementable,questionPK)

        questionCampo = input('Deseas añadir otro campo?(y/n) ')

        while True:
            if questionCampo == 'y' or questionCampo == 'n':
                break
            else:
                print('Solo puedes responder escriibiendo "y" para afirmar o "n" para negar')
                questionCampo = input('Deseas añadirle tablas a la base de datos?(y/n)')

        if questionCampo == 'y':
            addCampo(nameDB,nameTable)

def createTable(nameDB):
        nombreTable = input('Como quieres que se llama la tabla? ')
        nombreCampo = input('Como quieres que se llame el campo? ')
        tipoDato = input('Que tipo de dato quieres que sea? ')
        signos = input('Quieres que puedan introducirse signos?(y/n) ')

        while True:
            if signos == 'y' or signos == 'n':
                break
            else:
                print('Solo puedes responder escribiendo "y" para afirmar o "n" para negar')
                signos = input('Quieres que puedan introducirse signos?(y/n) ')

        if signos == 'n':
            signos = 'UNSIGNED'
        else:
            signos = ''


        incrementable = input('Deseas que sea auto incrementable?(y/n) ')

        while True:
            if incrementable == 'y' or incrementable == 'n':
                break
            else:
                print('Solo puedes responder escribiendo "y" para afirmar o "n" para negar')
                incrementable = input('Deseas que sea auto incrementable?(y/n)')

        if incrementable == 'y':
            incrementable = 'AUTO_INCREMENT'
        else:
            incrementable = ''

        questionPK = input('Quieres que sea Primary Key? ')

        while True:
            if questionPK == 'y' or questionPK == 'n':
                break
            else:
                print('Solo puedes responder escriibiendo "y" para afirmar o "n" para negar')
                questionPK = input('Quieres que sea Primary Key? ')    

        if questionPK == 'y':
            questionPK = 'PRIMARY KEY'
        elif questionPK == 'n':
            questionNull = input('Deseas que el dato sea nulo o no nulo?(null/not null)')  
            while True:
                if questionNull == 'null' or questionNull == 'not null':
                    break
                else:
                    print('Solo puedes responder escribiendo "null "o "not null"')
                    questionNull = input('Deseas que el dato sea nulo o no nulo?(null/not null)')     

            if questionNull == 'null':
                questionPK = 'NULL'
            else:
                questionPK = 'NOT NULL'  

        addTable(nameDB,nombreTable,nombreCampo,tipoDato,signos,incrementable,questionPK)

        questionCampo = input('Deseas añadir otro campo?(y/n) ')

        while True:
            if questionCampo == 'y' or questionCampo == 'n':
                break
            else:
                print('Solo puedes responder escriibiendo "y" para afirmar o "n" para negar')
                questionCampo = input('Deseas añadirle tablas a la base de datos?(y/n)')

        if questionCampo == 'y':
            addCampo(nameDB,nombreTable)



def createDB():
    nombreDB = input('Como quieres que se llama la base de datos?\n')

    create(nombreDB)

    showDB = show()

    print(tabulate(showDB,headers=['BASES DE DATOS'],tablefmt='psql'))


    question = input('Deseas añadirle tablas a la base de datos?(y/n)')

    while True:
        if question == 'y' or question == 'n':
            break
        else:
            print('Solo puedes responder escriibiendo "y" para afirmar o "n" para negar')
            question = input('Deseas añadirle tablas a la base de datos?(y/n)')


    if question == 'y':
        createTable(nombreDB)


    addDB = input('Deseas crear otra base de datos?(y/n)\n')
    while True:
        if addDB == 'y' or addDB == 'n':
            break
        else:
            print('Solo puedes responder escriibiendo "y" para afirmar o "n" para negar')
            addDB = input('Deseas crear otra base de datos?(y/n)\n')
        
    if addDB == 'y':
        createDB()



def deleteDB():
    showDB = show()

    print(tabulate(showDB,headers=['BASES DE DATOS'],tablefmt='psql'))

    nombreDB = input('Que base de datos desea eliminar? ')

    delete(nombreDB)

    newDB = show()

    print(tabulate(newDB,headers=['BASES DE DATOS'],tablefmt='psql'))

    choose = input('Deseas eliminar otra base de datos?(y/n) ')
    

    while True:
        if choose == 'y' or choose == 'n':
            break
        else:
            print('Solo puedes responder escriibiendo "y" para afirmar o "n" para negar')
            choose = input('Deseas eliminar otra base de datos?(y/n) ')

    if choose == 'y':
        deleteDB()




def updateTable():
        while True:
            showDB = show()

            print(tabulate(showDB,headers=['BASES DE DATOS'],tablefmt='psql'))

            chooseDB = input('Que base de datos deseas añadirle una o varias tablas? ')

            chooseCheck = False

            for i in showDB:
                if chooseDB == i[0]:
                    chooseCheck = True

            if chooseCheck == True:

                while True:
                    tables = showTable(chooseDB)

                    print(tabulate(tables,headers=['TABLAS'],tablefmt='psql'))

                    chooseTable = input('Que tabla deseas actualizar? ')

                    tableCheck = False    

                    for i in tables:
                        if chooseTable == i[0]:
                            tableCheck = True

                    if tableCheck == True:
                        data = showDataTable(chooseDB,chooseTable)
                        columns = showColumns(chooseDB,chooseTable)
                        print(tabulate(data,tablefmt='psql'))    
                        print(tabulate(columns,tablefmt='psql'))    

                        while True:
                            chooseColumn = input('Que columna deseas actualizar? ')
                            idName = input('Escribe el nombre de la columna que contiene el id: ')
                            datoColumn = input('Escribe el id de la columna a actualizar: ')
                            columnCheck = False
                            for i in columns:
                                if chooseColumn == i[0]:
                                    columnCheck = True   

                            if columnCheck == True:
                                dato = input('Escribe el nuevo dato: ') 
                                updateData(chooseDB,chooseTable,chooseColumn,dato,datoColumn,idName)
                                resultado = showUpdate(chooseDB,chooseTable,chooseColumn,datoColumn,idName)

                                print(tabulate(resultado,headers=['actualizacion'],tablefmt='psql'))
                                break
                            else:
                                print('Debes escribir una columna que exista.\n')

                        break                   
                    else:
                        print('Tabla no encontrada.Elige una tabla que exista.')


                end_update = input('Deseas actualizar otra columna?(y/n) ')

                while True:
                    if end_update == 'y' or end_update == 'n':
                        break
                    else:
                        print('Solo puedes responder con "y" para afirmar o "n" para negar.')
                        end_update = input('Deseas actualizar otra columna?(y/n) ')

                if end_update == 'n':
                    break
            else:
                print('Base de datos no encontrada.Elige una base de datos que exista.\n')
            
# ola = show()

# list = []
# listMuestra = []

# #print(tabulate(ola,headers=['Bases de datos']))

# for i in ola:
#     listMuestra.append(i)
#     list.append(i[0])


# print(tabulate(listMuestra,headers=['Bases de datos']))

# choose = input('escribe db que deseas eliminar: ')



# if choose not in list:
#     print('no se encuentra la db')
# else:
#     delete(choose)


# end = show()

# print(tabulate(end,headers=['Bases de datos']))


#print(tabulate(lista,headers=['cita','hola']))

#---------- menu ---------
list_menu = ['Crear base de datos','Crear tablas','Ver todas las bases de datos disponibles','Actualizar datos de una tabla','Eliminar una base de datos']

while True:
    print('-------- CRUD PYTHON / MYSQL --------')

    while True:
        try:
            for i in range(len(list_menu)):
                print(i,'-',list_menu[i])

            choose = int(input('\nEscoge la accion ingresando el numero que se encuntra del lado izquierdo: '))

            if choose >= 0 and choose <len(list_menu):
                break
            else:
                print('Debes elegir uno de los numero que se muestran anteriormente.')
        except ValueError:
            print('Debes escribir un numero.\n')

    
    if choose == 0:
         createDB()

    elif choose == 1:

        while True:
            showDB = show()

            print(tabulate(showDB,headers=['BASES DE DATOS'],tablefmt='psql'))

            chooseDB = input('Que base de datos deseas añadirle una o varias tablas? ')

            chooseCheck = False

            for i in showDB:
                if chooseDB == i[0]:
                    chooseCheck = True

            if chooseCheck == True:
                createTable(chooseDB)
                break
            else:
                print('Base de datos no encontrada.\n')

    elif choose == 2:
        showDB = show()
        print(tabulate(showDB,headers=['BASES DE DATOS'],tablefmt='psql'))

    elif choose == 3:

        updateTable()

    elif choose == 4:
        deleteDB()
    
    end_Programme = input('Deseas seguir en el programa?(y/n) ')
    while True:
        if end_Programme == 'y' or end_Programme == 'n':
            break
        else:
            print('Solo puedes responder escribiendo "y" para afirmar o n"" para negar')
            end_Programme = input('Deseas seguir en el programa?(y/n) ')

    if end_Programme == 'n':
        print('\n......')
        time.sleep(1)
        print('Gracias por utilizar nuestro programa.')
        break
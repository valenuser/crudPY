from tabulate import tabulate
import time


from db import createDB as create
from db import showDB as show
from db import deleteDB as delete
from db import createTable as addTable
from db import addCampo


#crear funcion para crear campos

def addCampo(nameDB,nameTable):
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
                questionPK = 'null'
            else:
                questionPK = 'not null'  

        addCampo(nameDB,nameTable,nombreCampo,tipoDato,signos,incrementable,questionPK)

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
                questionPK = 'null'
            else:
                questionPK = 'not null'  

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
list_menu = ['Crear base de datos','Crear tablas','Ver todas las bases de datos disponibles o los datos de una tabla','Actualizar datos de una tabla','Eliminar una base de datos o una tabla']

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
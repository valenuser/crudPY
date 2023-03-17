from tabulate import tabulate

from db import createDB as create
from db import showDB as show
from db import deleteDB as delete

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

print('-------- CRUD PYTHON / MYSQL --------')

list_menu = ['Crear base de datos o tablas','Ver todas las bases de datos disponibles o los datos de una tabla','Actualizar datos de una tabla','Eliminar una base de datos o una tabla']

print(len(list_menu))
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
        print('Debes escribir un numero.')

print(choose)
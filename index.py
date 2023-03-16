from tabulate import tabulate

from db import createDB as create
from db import showDB as show
from db import deleteDB as delete

ola = show()

list = []
listMuestra = []

#print(tabulate(ola,headers=['Bases de datos']))

for i in ola:
    listMuestra.append(i)
    list.append(i[0])


print(tabulate(listMuestra,headers=['Bases de datos']))

choose = input('escribe db que deseas eliminar: ')



if choose not in list:
    print('no se encuentra la db')
else:
    delete(choose)


end = show()

print(tabulate(end,headers=['Bases de datos']))


#print(tabulate(lista,headers=['cita','hola']))


from tabulate import tabulate

from db import createDB as create
from db import showDB as show

ola = show()

print(tabulate(ola,headers=['Bases de datos']))


#print(tabulate(lista,headers=['cita','hola']))


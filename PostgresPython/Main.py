import psycopg2
import Consulta as ObjConsulta
import archivo as ObjArchivo
op = input("Selecciona una opcion: ")
print("(1) Archivo 1")
print("(2) Archivo 2")
if op == "1":
    nombres = './nombres.txt' 
    listaNombres = ObjArchivo.archivo().Consulta(nombres)
    ObjConsulta.Consulta().Add(listaNombres)
elif op == "2":
    nombres2 = './nombres2.txt' 
    listaNombres2 = ObjArchivo.archivo().Consulta(nombres2)
    ObjConsulta.Consulta().Add(listaNombres2)    
else:
    print("Opcion invalida")

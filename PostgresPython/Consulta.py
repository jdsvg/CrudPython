from datetime import date
import psycopg2
import archivo as ObjArchivo

class Consulta:
    def __init__(self):
        self.datos={}
        self.nombresEncontrados = []
        self.dbVacia = True
        self.strNombre = ""
    def Conexion(self):
        #Global constant
        PSQL_HOST = "localhost"
        PSQL_PORT = "5432"
        PSQL_USER = "postgres"
        PSQL_PASS = "admin"
        PSQL_DB = "database1"
        #Connection
        connection_address = """
        host=%s port=%s user=%s password=%s dbname=%s
        """% (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
        connection = psycopg2.connect(connection_address)
        return (connection, connection.cursor())

    def Sql(self, consultaSQL):
            (connection, cursor) = self.Conexion()
            cursor.execute(consultaSQL)
            connection.commit()

    def Add(self, listado):
        for nombre in listado:
            (connection, cursor) = self.Conexion()
            SQL = "SELECT * FROM nombres;"
            cursor.execute(SQL)
            for nombreDB in cursor:
                self.dbVacia = False
                self.strNombre = str(nombreDB[0])
                if nombre in self.strNombre:
                    self.nombresEncontrados.append(nombre)   
        print("Nombres encontrados: ",self.nombresEncontrados)
        if self.dbVacia:
            print("Base de datos vacia")
            for nombre in listado:
                self.Sql(("INSERT INTO nombres(nombre) VALUES("+"'"+nombre+"'"+");"))###
        else:
            if self.nombresEncontrados:
                cont=0
                for nombre2 in listado:
                    if nombre2 == self.nombresEncontrados[cont]:
                        print(nombre2," repetido")
                        fecha = date.today()
                        fechaStr = str(fecha)
                        self.Sql(("INSERT INTO oldnombres(nombre, fecha) VALUES("+"'"+nombre2+"'"+","+"'"+fechaStr+"'"+");"))
                        cont+=1 
                    else:
                        self.Sql(("INSERT INTO nombres(nombre) VALUES("+"'"+nombre2+"'"+");"))
                        (connection, cursor) = self.Conexion()
                        print(nombre2," insertado")
                    #cont+=1    
            else:
                print("Lista vacia")
                self.Sql(("INSERT INTO nombres(nombre) VALUES("+"'"+nombre+"'"+");"))

        


#objConexion = Consulta()
#nombres = './nombres.txt' 
#nombres2 = './nombres2.txt'
#listaNombres = ObjArchivo.archivo().Consulta(nombres)
#listaNombres2 = ObjArchivo.archivo().Consulta(nombres2)
#objConexion.Add(listaNombres)
#objConexion.Add(listaNombres2)




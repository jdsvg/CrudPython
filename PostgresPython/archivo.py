from io import open
class archivo:

    def __init__(self):
        self.listaNombres = []
    
    def Lectura(self,f, variable ):
        if variable == "r":
            lector = open(f, 'r')
        elif variable == "w":
            lector = open(f, 'w')
        else:
            lector = open(f, 'rw')  
        return lector 

    def Consulta(self,f):
        lector = self.Lectura(f,"r")
        if f:
            for linea in lector:
                self.listaNombres.append(linea[:-2])
        return self.listaNombres
            




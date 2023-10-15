from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__ (self,nombre,edad,altura,sexo,años,goles,rojas,pierna):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,años)
        self._golesMarcados=goles
        self._tarjetasRojas=rojas
        self._piernaHabil=pierna
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,goles):
        self._golesMarcados=goles

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,rojas):
        self._tarjetasRojas=rojas

    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,pierna):
        self._piernaHabil=pierna

    def __str__(self):
        return "Mi nombre es " +self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+" Tengo "+self.getEdad()+" años de edad y llevo "+self.getAñosPracticando()+" años en el deporte"
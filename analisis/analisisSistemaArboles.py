import pandas as pd

from data.generators.generadorDatosSistemaArboles import generarDatosSistemaArboles

#PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameSistemaArboles():
    #traigo los datos generados en el mock
    datosSistemaArboles=generarDatosSistemaArboles()

    #construyo el Dataframe
    sistemaArbolesDF=pd.DataFrame(datosSistemaArboles, columns=['corregimientos','especies','hectareas','nombre','id'])

    #probando...
    #print(sistemaArbolesDF)

construirDataFrameSistemaArboles()
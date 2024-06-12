import pandas as pd

from data.generators.sostenibilidad import sostenibilidad

#PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameSostenibilidad():
    #traigo los datos generados en el mock
    datosSostenibilidad=sostenibilidad()

    #construyo el Dataframe
    SostenibilidadDF=pd.DataFrame(datosSostenibilidad,columns=['empresa','municipio','elemento','cantidad','tipo de persona'])


    #probando...
    #print(SostenibilidadDF)

construirDataFrameSostenibilidad()
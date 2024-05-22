import pandas as pd

from data.generators.generadorCalidadAire import generadorDatosCalidad

#PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameCalidadAire():
    #traigo los datos generados en el mock
    datosCalidadAire=generadorDatosCalidad()

    #construyo el Dataframe
    calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['comuna','tipo','muestra','ica','fecha','nombre','id'])

    #probando...
    print(calidadAireDF)

construirDataFrameCalidadAire()
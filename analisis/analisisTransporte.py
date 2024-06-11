import pandas as pd

from data.generators.generadorDatosTransporte import generadorDatosTransporte
#PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameTransporte():
    #traigo los datos generados en el mock
    datosTransporte=generadorDatosTransporte()

    #construyo el Dataframe
    TransporteDF=pd.DataFrame(datosTransporte,columns=['Medio','Frecuencia','Genero','Id','Nombre'])

    #probando...
    print(TransporteDF)

construirDataFrameTransporte()
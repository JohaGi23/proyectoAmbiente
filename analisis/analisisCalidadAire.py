import pandas as pd
from data.generators.generadorCalidadAire import generadorDatosCalidad
from helpers.generadorTabla import crearTablaHtml

# PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameCalidadAire():
  #traigo los datos generados en el MOCK
  datosCalidadAire=generadorDatosCalidad()
  
  #construyo el dataframe
  calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['Comunas','tplob','muestra','ICA','fecha','nombre','id'])
  print(calidadAireDF)
  crearTablaHtml(calidadAireDF,"calidadAire")
  
#probando
construirDataFrameCalidadAire()
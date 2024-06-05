import pandas as pd
from data.generators.generadorCalidadAire import generadorDatosCalidad
from helpers.generadorTabla import crearTablaHtml

# PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameCalidadAire():
  #traigo los datos generados en el MOCK
  datosCalidadAire=generadorDatosCalidad()
  
  #construyo el dataframe
  calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['Comunas','ttlplob','muestra','ICA','fecha','nombre','id'])
  #probando
  #print(calidadAireDF)
  #crearTablaHtml(calidadAireDF,"calidadAire")
  
  #Limpiando el dataframe
  
  #1. Limpiando (reemplazando valores)
  #calidadAireDF.replace('-',pd.NA,inplace=True)
  #calidadAireDF.replace('sin',pd.NA,inplace=True)
  #probando
  #print("\n")
  #print(calidadAireDF)
  
  #2. Limpiando (eliminando valores)
  calidadAireDF.replace('sin',pd.NA,inplace=True)
  calidadAireDF.dropna(inplace=True)
  
  #3. Filtrando datos para depurar la información
  #FILTRAR DATOS ES OBTENER NUEVOS DATAFRAMES
  #AL APLICAR CONDICIONES LÓGICAS
  
  #CONTAR DATOS
  
  #CONSULTAR DATOS ESPECÍFICOS
  filtraICAPositivo= calidadAireDF.query("(ICA>50) and (ICA <50)")
  filtraICAModerado= calidadAireDF.query("(ICA>=50) and (ICA <70)")
  filtraICAPeligroso= calidadAireDF.query("(ICA>=70)")
  #print(filtraICAPositivo)
  #print("\n")
  #print(filtraICAPositivo)
  #print("\n")
  print(filtraICAPositivo)
  #print("\n")

  
  
#probando
construirDataFrameCalidadAire()

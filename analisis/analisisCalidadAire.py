import pandas as pd
import matplotlib.pyplot as plt 
from data.generators.generadorCalidadAire import generadorDatosCalidad
from helpers.generadorTabla import crearTablaHtml

# PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameCalidadAire():
  #traigo los datos generados en el MOCK
  datosCalidadAire=generadorDatosCalidad()
  
  #construyo el dataframe
  calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['Comunas','tplob','muestra','ICA','fecha','nombre','id'])

  #limpiando el dataframe

  #1. Limpiando (reemplazando valores)
  #calidadAireDF.replace('-', pd.NA, inplace=True)
  #calidadAireDF.replace('sin', pd.NA, inplace=True)

  #2. limpiando (eliminando valores)
  calidadAireDF.replace('sin', pd.NA, inplace=True)
  calidadAireDF.dropna(inplace=True)

  #3. Filtrando datos para depurar la informacion
  #FILTRAR DTOS ES OBTENER NUEVOS DATFRAMES
  # AL APLICAR CONDICIONES LOGICAS

  #CONTAR DATOS

  #CONSULTAR DATOS ESPECIFICOS
  #filtroPositivo=calidadAireDF.query("(ICA>=20) and (ICA<50)")
  #filtroICAModerado=calidadAireDF.query("(ICA>=50) and (ICA<70)")
  # flitroICAPeligroso=calidadAireDF.query("(ICA>=70)").value_counts()

  #print(filtroPositivo)
  #print('\n')
  #print(filtroICAModerado)
  #print('\n')
  # print(flitroICAPeligroso)
  print('\n')

  #agrupando datos
  datosAgrupados=calidadAireDF.groupby("Comunas")["ICA"].mean()

  #graficando datos
  plt.figure(figsize=(20,20))
  datosAgrupados.plot(kind='bar',color='green')
  plt.title('Calidad de aire por comuna en Medellín')
  plt.xlabel('Comunas')
  plt.ylabel('ICA(Indice Calidad de Aire)')
  plt.grid(True)
  plt.xticks(rotation=45)
  plt.savefig('./assets/img/calidadAire.png',format='png',dpi=300)
  plt.show()

  #probando...
  
  #crearTablaHtml(calidadAireDF,"calidadAire")
  
#probando
construirDataFrameCalidadAire()
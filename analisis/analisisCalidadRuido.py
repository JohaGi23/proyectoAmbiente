import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorRuido import generarRuido
from helpers.generadorTabla import crearTablaHtml


# PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameRuido():
  #traigo los datos generados en el MOCK
  datosRuido=generarRuido()
  
  #construyo el dataframe
  ruidoDF=pd.DataFrame(datosRuido, columns=['Comuna','tllpoblacion',"tñmuestra","dbDia","dbNoche","fecha","nombre"])
  #print(ruidoDF)

  #limpiando el dataframe

  #1. Limpiando (reemplazando valores)
  ruidoDF.replace('-', pd.NA, inplace=True)
  ruidoDF.replace('sin', pd.NA, inplace=True)

  #2. limpiando (eliminando valores)
  ruidoDF.replace('sin', pd.NA, inplace=True)
  ruidoDF.dropna(inplace=True)

  #3. Filtrando datos para depurar la informacion
  #FILTRAR DTOS ES OBTENER NUEVOS DATFRAMES
  # AL APLICAR CONDICIONES LOGICAS

  #CONTAR DATOS

  #CONSULTAR DATOS ESPECIFICOS
  #filtroPositivo=ruidoDF.query("(tñmuestra>=20) and (tñmuestra<50)")
  #filtroMuestraModerado=ruidoDF.query("(tñmuestra>=50) and (tñmuestra<70)")
  #filtroMuestraPeligroso=ruidoDF.query("(tñmuestra>=70)").value_counts()

  #print(filtroPositivo)
  #print('\n')
  #print(filtroMuestraModerado)
  #print('\n')
  # print(flitroMuestraPeligroso)
  print('\n')

  #agrupando datos
  datosAgrupados=ruidoDF.groupby("Comuna")["dbDia"].mean()

  #graficando datos
  plt.figure(figsize=(20,20))
  datosAgrupados.plot(kind='bar',color='green')
  plt.title('Calidad de ruido generado en el dia en comunas de Medellín')
  plt.xlabel('Comuna')
  plt.ylabel('Ruido x dia')
  plt.grid(True)
  plt.xticks(rotation=45)
  plt.savefig('./assets/img/calidadRuido.png',format='png',dpi=300)
  plt.show()

  #probando...
  
  crearTablaHtml(ruidoDF,"calidadAire")
  
#probando
construirDataFrameRuido()
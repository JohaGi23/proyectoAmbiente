import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorDatosTransporte import generadorDatosTransporte
from helpers.generadorTabla import crearTablaHtml
#PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameTransporte():
    #traigo los datos generados en el mock
   datosTransporte=generadorDatosTransporte()

    #construyo el Dataframe
   TransporteDF=pd.DataFrame(datosTransporte,columns=['Medio','Frecuencia','Genero','Id','Nombre'])

     #limpiando el dataframe

  #1. Limpiando (reemplazando valores)
   TransporteDF.replace('-', pd.NA, inplace=True)
   TransporteDF.replace('sin', pd.NA, inplace=True)

  #2. limpiando (eliminando valores)
   TransporteDF.replace('sin', pd.NA, inplace=True)
   TransporteDF.dropna(inplace=True)

  #3. Filtrando datos para depurar la informacion
  #FILTRAR DTOS ES OBTENER NUEVOS DATFRAMES
  # AL APLICAR CONDICIONES LOGICAS

  #CONTAR DATOS

  #CONSULTAR DATOS ESPECIFICOS
  #filtroPositivo=TransporteDF.query("(Frecuencia>=20) and (Frecuencia<50)")
  #filtroFrecuenciaModerado=TransporteDF.query("(Frecuencia>=50) and (Frecuencia<70)")
  #filtroFrecuenciaPeligroso=TransporteDF.query("(Frecuencia>=70)").value_counts()

  #print(filtroPositivo)
  #print('\n')
  #print(filtroFrecuenciaModerado)
  #print('\n')
  # print(flitroFrecuenciaPeligroso)
   print('\n')

  #agrupando datos
   datosAgrupados=TransporteDF.groupby("Medio")["Frecuencia"].mean()

      #graficando datos
   plt.figure(figsize=(20,20))
   datosAgrupados.plot(kind='bar',color='green')
   plt.title('Frecuencia de Medio de Transporte utilizado en Medellín')
   plt.xlabel('Medio')
   plt.ylabel('Frecuencia')
   plt.grid(True)
   plt.xticks(rotation=45)
   plt.savefig('./assets/img/FrecuenciaT.png',format='png',dpi=300)
   plt.show()

      #probando...
      
   try:
    crearTablaHtml(TransporteDF, "transporte")
   except Exception as e:
    print("Error al crear la tabla HTML:", e)

         #probando...
   print(TransporteDF)

construirDataFrameTransporte()
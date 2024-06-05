import pandas as pd
from data.generators.generadorRuido import generarRuido

# PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameRuido():
  #traigo los datos generados en el MOCK
  datosRuido=generarRuido()
  
  #construyo el dataframe
  ruidoDF=pd.DataFrame(datosRuido, columns=['Comuna','tllpoblacion',"tñmuestra","dbDia","dbNoche","fecha","nombre",])
  #print(ruidoDF)
  
#probando
construirDataFrameRuido()
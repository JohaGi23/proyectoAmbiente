import pandas as pd

from data.generators.generadorDatosSistemaArboles import generarDatosSistemaArboles

#PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameSistemaArboles():
    #traigo los datos generados en el mock
    datosSistemaArboles=generarDatosSistemaArboles()

    #construyo el Dataframe
    sistemaArbolesDF=pd.DataFrame(datosSistemaArboles, columns=['corregimientos','especies','hectareas','nombre','id'])



    sistemaArbolesDF.replace('-', pd.NA, inplace=True)
    sistemaArbolesDF.replace('sin', pd.NA, inplace=True)

    sistemaArbolesDF.replace('sin', pd.NA, inplace=True)
    sistemaArbolesDF.dropna(inplace=True)

    print('\n')

    datosAgrupados=sistemaArbolesDF.groupby("Comuna")["dbDia"].mean()


    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Calidad de arboles por comuna')
    plt.xlabel('Comuna')
    plt.ylabel('Tamaño de Muestra')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/calidadArboles.png',format='png',dpi=300)
    plt.show()

    crearTablaHtml(sistemaArbolesDF,"SistemaArboles")

    #probando...
    #print(sistemaArbolesDF)    
construirDataFrameSistemaArboles()
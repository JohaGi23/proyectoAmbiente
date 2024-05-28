import random 
#NOMBREEDICIFIO
def generarRuido():
  listaDatos=[]
  for i in range(500):
    comuna=random.choice(['comuna 1 popular','comuna 2 sta cruz','comuna 12 la america',
												'comuna 4 aranjuez','comuna 13 san javier', 'comuna 16 belen'])
    totalPoblacion=random.choice(['3000','4500','5000','10000'])
    tamanoMuestra=random.choice(['1000','2000','3500','6000'])
    decibelesDia= random.randint(0,150)
    decibelesNoche = random.randint(0,100)
    fechaEncuesta= random.choice(["23/06/2024","22/06/2024","21/06/2024","20/05/2024"])
    nombreEncuestado=random.choice(["Pedro Paramos","Sandra Mor","Kevin Albeiro",
																	"Valentina Mor", "Juam Jimeno"])
    datosRuido=[comuna,totalPoblacion,tamanoMuestra,decibelesDia,decibelesNoche,fechaEncuesta,nombreEncuestado]
    listaDatos.append(datosRuido)
  return listaDatos
  



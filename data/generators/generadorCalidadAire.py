#Rutina para generar de forma aleatoria
#multiples datos con python

import random 
listaDatos=[]

def generadorDatosCalidad():
	for i in range(1000):
		comuna=random.choice(['comuna 1 popular','comuna 2 sta cruz','comuna 12 la america',
												'comuna 4 aranjuez','comuna 13 san javier', 'comuna 16 belen','sin','-'])
		totalPoblacion=random.choice(['3000','4500','5000','10000'])
		tamanoMuestra=random.choice(['1000','2000','3500','6000'])
		ica=random.randint(20,100)
		fecha=random.choice(["2024-05-14","2024-05-15"])
		nombreEncuestado=random.choice(["Pedro Paramos","Sandra Mor","Kevin Albeiro",
																	"Valentina Mor", "Juam Jimeno"])
		id=random.randint(0,10000000)
		calidadAire=[comuna,totalPoblacion,tamanoMuestra,ica,fecha,nombreEncuestado,id]
		listaDatos.append(calidadAire)
	return listaDatos



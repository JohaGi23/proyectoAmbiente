import random

listaDatos=[]

def generadorDatosTransporte():
	for i in range (1000):
		medioMasUtlizado = random.choice(['metro','bici','bus','privado','moto'])
		frecuenciaUsoSemanal = random.randint(1,20)
		genero = random.choice(['hombre','mujer'])
		id= random.randint(1,1000000)
		nombreEncuestado=random.choice(["Pedro Paramos","Sandra Mor","Kevin Albeiro",
																	"Valentina Mor", "Juam Jimeno"])
		datosTransporte = [medioMasUtlizado,frecuenciaUsoSemanal,genero,id,nombreEncuestado]
		listaDatos.append(datosTransporte)
	return datosTransporte


print(generadorDatosTransporte())

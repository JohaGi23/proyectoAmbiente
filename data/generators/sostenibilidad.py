import random
ListaDatos=[]

def sostenibilidad():
	for i in range (1000):
		empresa=random.choice(['dandone', 'HP inc', 'l oreal', 'unilever','UPM Kymmene'])
		municipio=random.choice(['barbosa', 'copacabana', 'girardota', 'bello', 'itagui'])
		elementomasreciclado=random.choice (['acero'])
		cantidadreciclada=random.choice ([500])
		tipodepersona=random.choice (['natural', 'juridica'])
		sostenibilidad=[empresa,municipio,elementomasreciclado,cantidadreciclada,tipodepersona]

		ListaDatos.append(sostenibilidad)
	return ListaDatos

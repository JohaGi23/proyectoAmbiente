import random
listaDatos=[]
def generarDatosSistemaArboles():
	for i in range (500):
		corregimientos=random.choice([
			'San Antonio de Prado',
			'San Cristóbal',
			'Altavista',
			'San Sebastián de Palmitas',
			'Santa Elena',
			'San Javier',
			'San Juan de la Tasajera',
			'San Antonio de Prado',
			'Santa Elena',
			'Altavista',
			'San Cristóbal',
			'San Sebastián de Palmitas',
			'San Antonio de Prado',
			'San Javier',
			'San Juan de la Tasajera'])
		hectareasSembradas=random.choice(['3000','4500','5000','10000'])
		especieSembrada=random.choice([
			'Roble',
			'Pino',
			'Ceiba',
			'Nogal',
			'Cedro',
			'Arce',
			'Fresno',
			'Olivo',
			'Palma',
			'Álamo',
			'Abeto',
			'Manzano',
			'Chopo',
			'Almendro',
			'Eucalipto'])
		nombreEncuestado=random.choice(['pedro paramo','sandra mor','martina la peligrosa','kevin albeiro','valentina mor','juan jimeno'])
		id=random.randint(0,1000000)
		sistemaArboles=[corregimientos,hectareasSembradas,especieSembrada,nombreEncuestado,id]

		listaDatos.append(sistemaArboles)
	return listaDatos

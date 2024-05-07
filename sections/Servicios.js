export function Servicios() {
	const objetoDOM = document;
	const pagina = `
	<section>
			<div class="fondo">
				<h1 class="title">Raices verdes</h1>
				<h2 class="info">Nuestra misión es proporcionar soluciones innovadoras y
					efectivas para el monitoreo ambiental, con el fin de contribuir al
					desarrollo sostenible de la región.</h2>
			</div>
		</section>
		<section id="servicios">
			<div class="container">
				<div class="info">
					<h1>Servicios</h1>
				</div>
				<div class="servicios">
					<div class="servicio1" style="text-align: center;">
						<img src="./assets/img/asesoria.png"
							style="height: 100px; width: 100px;" alt="">
						<h3>Asesoria</h3><br>
						<button class="boton">Ver mas</button>
					</div>
					<div class="servicio1" style="text-align: center;">
						<img src="./assets/img/monitoreo.png"
							style="height: 100px; width: 100px;" alt="">
						<h3>Monitoreo</h3><br>
						<button class="boton">Ver mas</button>
					</div>
					<div class="servicio1" style="text-align: center;">
						<img src="./assets/img/sostanze-tossiche-negli-indumenti.png"
							style="height: 100px; width: 100px;" alt="">
						<h3>Analisis de emisiones</h3><br>
						<button class="boton">Ver mas</button>
					</div>
				</div>
			</div>
		</section>
	`;
	objetoDOM.getElementById("serviciosKevin").innerHTML = `${pagina}`;
}

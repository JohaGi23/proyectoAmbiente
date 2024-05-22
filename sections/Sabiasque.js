export function Sabiasque() {
	const objetoDOM = document;
	const pagina = `

<section class="sabiasque" id="sabiasque">
			<h1>Análisis de Datos sobre Sostenibilidad Ambiental en Medellín</h1>
			<br>
			<h1>¿Sabías que?</h1>
			<ul>
				<li>
					<img src="/assets/img/DEFORESTACION.jpg" alt="Imagen Descriptiva"
						id="imagen1">
					<h3>¿Cuál es el impacto de la deforestación en Medellín?</h3>
					<p>La deforestación en Medellín contribuye a la pérdida de
						biodiversidad, aumento de la erosión del suelo y alteración del
						ciclo
						hidrológico, lo que puede llevar a inundaciones y deslizamientos de
						tierra.</p>
				</li>
				<li>
					<img src="/assets/img/MEDIDAS.jpg" alt="Imagen Descriptiva"
						id="imagen3">
					<h3>¿Qué medidas se están tomando para promover la sostenibilidad en
						Medellín?</h3>
					<p>En Medellín, se están implementando medidas como la expansión del
						transporte público, la promoción de la energía renovable y la
						educación ambiental para fomentar prácticas más sostenibles en la
						comunidad.</p>
				</li>
				<li>
					<img src="/assets/img/CONTAMINACION.jpg" alt="Imagen Descriptiva"
						id="imagen2">
					<h3>¿Cómo afecta la contaminación del aire a la salud de los
						habitantes
						de Medellín?</h3>
					<p>La contaminación del aire en Medellín está asociada con problemas
						respiratorios, como asma y bronquitis, así como con enfermedades
						cardiovasculares. Además, puede agravar condiciones médicas
						preexistentes.</p>
				</li>

			</ul>
		</section>
		<!--Aquí comienza el formulario de comentarios-- >
	<section id="comentarios">
		<h2>¿Qué dato curioso tienes sobre la sostenibilidad en Medellín?</h2>
		<form id="formulario-comentario">
			<label for="nombre">Nombre:</label><br>
				<input type="text" id="nombre" name="nombre" required><br>
					<label for="comentario">Comentario:</label><br>
						<textarea id="comentario" name="comentario" required></textarea><br>
							<button type="submit">Enviar</button>
						</form>
						<div id="comentarios-anteriores">
							<!-- esto es cuando ya le pongamos el js -->
						</div>

					</section>
	`;
	objetoDOM.getElementById("sabiasqueJoana").innerHTML = `${pagina}`;
}







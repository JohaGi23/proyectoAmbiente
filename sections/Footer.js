export function Footer() {
	const objetoDOM = document;
	const pagina = `
	<p>&copy; 2024 Análisis de Datos sobre Sostenibilidad Ambiental en Medellín
	</p>
	`;
	objetoDOM.getElementById("footer").innerHTML = `${pagina}`;
}


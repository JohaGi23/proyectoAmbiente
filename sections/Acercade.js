export function Acercade() {
	const objetoDOM = document;
	const pagina = `
	<div class="contenedor">
			<div class="tarjeta">
				<figure>
					<img src="../assets/perfiles/perfil-ricardo.jpeg" alt="">
				</figure>
				<div class="contenido">
					<h4 class="nombre">Ricardo Segura</h4>
					<p class="descripcion">Desarrollador Backend con
						C#,
						SQLServer y Frontend con Angular 17</p>
					<a href="https://github.com/rsegura09" target="_blank">Perfil
						GitHub</a>
				</div>
			</div>


			<div class="tarjeta">
				<figure>
					<img src="../assets/perfiles/perfil-joana.png" alt="">
				</figure>
				<div class="contenido">
					<h4 class="nombre">Leidy Johana Giraldo</h4>
					<p class="descripcion">Desarrollador Backend con
						C#,
						SQLServer y Frontend con Angular 17</p>
					<a href="https://github.com/JohaGi23" target="_blank">Perfil
						GitHub</a>
				</div>
			</div>


			<div class="tarjeta">
				<figure>
					<img src="../assets/perfiles/perfil-kevin.png" alt="">
				</figure>
				<div class="contenido">
					<h4 class="nombre">Kevin Diaz</h4>
					<p class="descripcion">Desarrollador Backend con
						C#,
						SQLServer y Frontend con Angular 17</p>
					<a href="https://github.com/kevinDiaz0" target="_blank">Perfil
						GitHub</a>
				</div>
			</div>


			<div class="tarjeta">
				<figure>
					<img src="../assets/perfiles/perfil-mariana.png" alt="">
				</figure>
				<div class="contenido">
					<h4 class="nombre">Mariana Solar Misas</h4>
					<p class="descripcion">Desarrollador Backend con
						C#,
						SQLServer y Frontend con Angular 17</p>
					<a href="https://github.com/vhaf" target="_blank">Perfil GitHub</a>
				</div>
			</div>
		</div>
	`;
	objetoDOM.getElementById("mainAcercade").innerHTML = `${pagina}`;
}


document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'http://127.0.0.1:8000/api/turnos/';
    const especialidadesUrl = 'http://127.0.0.1:8000/api/especialidades/'; // Ajusta la URL según tu API

    async function fetchEspecialidades() {
        try {
            const response = await fetch(especialidadesUrl);
            const data = await response.json();
            const select = document.createElement('select');
            select.id = 'especialidad';
            select.required = true;

            // Crear la opción predeterminada
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.textContent = 'Seleccionar especialidad';
            select.appendChild(defaultOption);

            // Agregar las opciones de especialidad
            data.forEach(especialidad => {
                const option = document.createElement('option');
                option.value = especialidad.id; // O usa el campo apropiado
                option.textContent = especialidad.nombre;
                select.appendChild(option);
            });

            // Reemplazar el contenedor del select
            document.getElementById('especialidad-container').appendChild(select);
        } catch (error) {
            console.error('Error fetching especialidades:', error);
        }
    }   

    // Función para obtener y mostrar los turnos
    async function fetchTurnos() {
        try {
            // Suponiendo que has guardado el token en localStorage después del login
            const token = localStorage.getItem('jwtToken'); // O usa la forma en que almacenas el token
    
            const response = await fetch(apiUrl, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}` // Agregar el token JWT aquí
                }
            });
            
            const data = await response.json();
            const list = document.getElementById('turno-list');
            list.innerHTML = '';
            data.forEach(turno => {
                const item = document.createElement('li');
                item.textContent = `${turno.nombre} - ${turno.especialidad} - ${turno.fecha} - ${turno.hora}`;
                list.appendChild(item);
            });
        } catch (error) {
            console.error('Error fetching turnos:', error);
        }
    }

    // Función para manejar el envío del formulario
    document.getElementById('turno-form').addEventListener('submit', async (event) => {
        event.preventDefault();
        
        // Obtener valores del formulario
        const nombre = document.getElementById('nombre').value;
        const especialidad = document.getElementById('especialidad').value;
        const fecha = document.getElementById('fecha').value;
        const hora = document.getElementById('hora').value;
    
        console.log({ nombre, especialidad, fecha, hora }); // Verifica los valores obtenidos
    
        // Enviar datos al servidor
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nombre,
                    especialidad,
                    fecha,
                    hora
                }),
            });
    
            if (response.ok) {
                console.log('Turno agregado exitosamente'); // Mensaje de éxito
                fetchTurnos(); // Actualizar la lista de turnos
                document.getElementById('turno-form').reset(); // Limpiar el formulario
            } else {
                console.error('Error adding turno:', response.statusText);
                const errorText = await response.text();
                console.error('Response text:', errorText); // Verifica el mensaje de error
            }
        } catch (error) {
            console.error('Error adding turno:', error);
        }
    });

    // Inicializar la página cargando los turnos existentes
    fetchEspecialidades();
    fetchTurnos();
});
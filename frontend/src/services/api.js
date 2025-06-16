const baseURL = "http://localhost:8000/api/";

export async function getPacientes() {
  const response = await fetch(`${baseURL}Pacientess/`, {
    method: 'GET',
    credentials: 'include',  // 👈 Esto es lo que permite enviar la cookie de sesión
  });

  if (!response.ok) {
    throw new Error("Error al obtener Pacientes");
  }

  return await response.json();
}

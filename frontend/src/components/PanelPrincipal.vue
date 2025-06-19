<template>
  <template>
  <div>
    <h2>Usuarios desde el backend</h2>
    <p v-if="error">{{ error }}</p>
    <ul v-else>
      <li v-for="usuario in usuarios" :key="usuario.id">
        {{ usuario.nombre_paciente }}
      </li>
    </ul>
  </div>
</template>

  <div class="panel-principal">
    <!-- Header -->
    <div class="header">
      <div class="left-group">
        <router-link to="/panel">
          <img src="@/assets/cerebro.png" alt="Logo" class="logo-img" />
        </router-link>
        <div class="search-section">
          <div class="search-container">
            <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none">
              <path d="M21 21L16.514 16.506M19 10.5C19 15.194 15.194 19 10.5 19C5.806 19 2 15.194 2 10.5C2 5.806 5.806 2 10.5 2C15.194 2 19 5.806 19 10.5Z"
                stroke="#9CA3AF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <input
              type="text"
              placeholder="Buscar..."
              v-model="searchQuery"
              @input="buscarPaciente"
            />
          </div>
        </div>
      </div>
      <button
        class="add-button"
        @click="addPatient"
        title="Agregar paciente nuevo"
      >
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
          <path d="M12 5V19M5 12H19" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <div class="user-section">
        <div class="user-info">
          <span class="user-name">{{ userName }}</span>
          <span class="user-role">{{ userRole }}</span>
        </div>
        <div class="user-avatar" @click="showProfileModal = true" style="cursor:pointer" title="Ver perfil">
          <img src="@/assets/perfil.png" alt="Avatar" class="profile-pic"/>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <div class="table-container">
        <div class="table-header">
          <div class="header-cell">Nombre del paciente</div>
          <div class="header-cell">ID</div>
          <div class="header-cell">Acción</div>
        </div>
        <div class="table-body">
          <div class="table-row" v-for="patient in usuarios" :key="patient.id">
            <div class="cell patient-name">{{ patient.nombre_paciente }}</div>
            <div class="cell patient-id">{{ patient.id }}</div>
            <div class="cell actions">
              <button class="action-button" @click="viewDetails(patient)">
                [Ver detalles]
              </button>
              <button class="icon-btn" @click="downloadPDF(patient)" title="Descargar PDF">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                  <path d="M12 16v5m-3 0h6M6 12V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-8a2 2 0 0 1-2-2v-7zm6-2v-4M9 10V6m6 4V6" stroke="#0059af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
              <button class="icon-btn" @click="removePatient(patient)" title="Eliminar">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                  <path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2m2 0v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6m3 6v6m4-6v6m4-6v6"
                        stroke="#e11d48" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODAL historia clínica -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal modal-scroll">
        <button class="modal-close" @click="closeModal" title="Cerrar">
          &times;
        </button>
        <h2 class="modal-title">Nueva historia clínica</h2>
        <form @submit.prevent="saveNewPatient">
          <label>
            ID:
            <input v-model="newPatient.id" />
          </label>
          <label>
            Nombre del paciente:
            <input v-model="newPatient.nombre_paciente" />
          </label>
          <label>
            Edad:
            <input v-model="newPatient.edad" />
          </label>
          <label>
            Género:
            <select v-model="newPatient.genero" required>
              <option value="">Selecciona una opción</option>
              <option value="femenino">Femenino</option>
              <option value="masculino">Masculino</option>
              <option value="otro">Otro</option>
            </select>
          </label>
          <label>
            Fecha de nacimiento:
            <input type="date" v-model="newPatient.fecha_nacimiento" />
          </label>
          <label>
            Motivo de consulta:
            <textarea v-model="newPatient.motivo_consulta" />
          </label>
          <label>
            Amnamnesis psiquiátrica:
            <textarea v-model="newPatient.amnesis_psiquiatrica" />
          </label>
          <label>
            Tratamiento:
            <textarea v-model="newPatient.tratamiento" />
          </label>
          <label>
            Plan terapéutico:
            <textarea v-model="newPatient.plan_terapeutico" />
          </label>
          <label>
            Fecha de ingreso:
            <input type="date" v-model="newPatient.fecha_ingreso" />
          </label>
          <label>
    <!-- MODAL para agregar evento -->
     <div v-if="showEventModal" class="modal-overlay">
      <div class="modal">
        <button class="modal-close" @click="cerrarModalEvento">&times;</button>
        <h2 class="modal-title">Agregar evento</h2>
        <label>
          Fecha:
          <input type="date" v-model="newEvent.fecha" required>
        </label>
        <label>
          Nombre del médico:
          <input v-model="newEvent.medico" required>
        </label>
        <label>
          Observación:
          <textarea v-model="newEvent.observacion" required rows="3"></textarea>
        </label>
        <div class="modal-actions">
          <button type="button" class="modal-save" @click="guardarEvento">Guardar</button>
          <button type="button" class="modal-cancel" @click="cerrarModalEvento">Cancelar</button>
        </div>
      </div>
    </div>

            Eventos:
            <textarea v-model="eventosComoTexto" readonly rows="2" style="background:#f4f4f4; color:#333;" />
            <button type="button" class="modal-save" @click="abrirModalEvento" style="margin-top:6px;">
              Agregar evento
            </button>
            
          </label>
          <div class="modal-actions">
            <button type="submit" class="modal-save">Guardar</button>
            <button type="button" class="modal-cancel" @click="closeModal">Cancelar</button>
          </div>
        </form>
      </div>
    </div>

    

    <!-- PANEL DE PERFIL  -->
    <div v-if="showProfileModal">
      <div class="profile-panel-overlay" @click.self="showProfileModal = false"></div>
      <div class="profile-panel">
        <!-- Flecha del tooltip -->
        <div class="profile-panel-arrow"></div>
        
        <!-- Opciones directamente -->
        <div class="profile-options">
          <button class="profile-option" @click="goToSettings">
            <div class="profile-option-icon settings-icon">
              <svg width="20" height="20" fill="none" viewBox="0 0 24 24">
                <path d="M12 15.5A3.5 3.5 0 1 0 12 8.5a3.5 3.5 0 0 0 0 7zm6.16-2.32l1.42-1.42a1 1 0 0 0 0-1.42l-1.13-1.13c.1-.36.15-.73.15-1.11s-.05-.75-.15-1.11l1.13-1.13a1 1 0 0 0 0-1.42l-1.42-1.42a1 1 0 0 0-1.42 0l-1.13 1.13A6.99 6.99 0 0 0 13 3.05V2a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v1.05c-.36.05-.71.13-1.05.23l-1.13-1.13a1 1 0 0 0-1.42 0L3.34 5.04a1 1 0 0 0 0 1.42l1.13 1.13c-.1.36-.15.73-.15 1.11s.05.75.15 1.11l-1.13 1.13a1 1 0 0 0 0 1.42l1.42 1.42a1 1 0 0 0 1.42 0l1.13-1.13c.34.1.7.18 1.05.23V22a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V17.95c.36-.05.71-.13 1.05-.23l1.13 1.13a1 1 0 0 0 1.42 0l1.42-1.42a1 1 0 0 0 0-1.42l-1.13-1.13c.1-.36.15-.73.15-1.11s-.05-.75-.15-1.11z"
                  stroke="currentColor" stroke-width="1.5" />
              </svg>
            </div>
            <span>Ajustes</span>
          </button>
          
          <button class="profile-option logout-option" @click="logout">
            <div class="profile-option-icon logout-icon">
              <svg width="20" height="20" fill="none" viewBox="0 0 24 24">
                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <span>Cerrar sesión</span>
          </button>
        </div>
      </div>
    </div>
    <!-- FIN PANEL PERFIL -->
  </div>
</template>

<script>
import jsPDF from 'jspdf'
export default {
  name: 'PanelPrincipal',
  data() {
    return {
      searchQuery: "",
      usuarios: [],
      showModal: false,
      showProfileModal: false,
      error: null,
      newPatient: {
      id: '',
      nombre_paciente: '',
      edad: '',
      genero: '',
      fecha_nacimiento: '',
      motivo_consulta: '',
      amnesis_psiquiatrica: '',
      tratamiento: '',
      plan_terapeutico: '',
      fecha_ingreso: '',
      eventos: []
    },
      showEventModal: false,
      newEvent: {                      
      fecha: '',
      medico: '',
      observacion: ''
    },
    }
  },
  mounted() {
        this.userName = localStorage.getItem('medicoNombre') || 'Nombre no disponible';
        this.userRole = localStorage.getItem('medicoPuesto') || 'Rol no disponible';
        fetch("http://127.0.0.1:8000/pacientes/api/pacientes/lista")
          .then(response => response.json())
          .then(data => {
            this.usuarios = data.pacientes;
            console.log("Usuarios:", this.usuarios);
          })
          .catch(error => {
            console.error("Error al obtener usuarios:", error);
            this.error = "Hubo un error al cargar los pacientes.";
          });
      },
  methods: {
    goToPanel() {
      this.$router.push('/panel');
    },
    closeModal() {
      this.showModal = false;       // Oculta el modal
      this.resetNewPatient();       // Limpia los campos (opcional, pero útil)
    },
    abrirModalEvento() {
      this.newEvent = { fecha: '', medico: '', observacion: '' }; 
      this.showEventModal = true;
    },
    cerrarModalEvento() {
      this.showEventModal = false;
    },
    guardarEvento() {
      if (!this.newEvent.fecha || !this.newEvent.medico || !this.newEvent.observacion) {
        alert("Completa todos los campos del evento.");
        return;
      }
      this.newPatient.eventos.push({ ...this.newEvent }); 
      this.showEventModal = false;
    },


    
    viewDetails(patient) {
      this.$router.push({ name: 'VerDetalles', params: { id: patient.id } });
    },
     async downloadPDF(patient) {
  try {
    const response = await fetch(patient.url);
    if (!response.ok) throw new Error("Error al obtener detalles del paciente");

    const data = await response.json();

    const doc = new jsPDF();
    let y = 20;

    doc.setFontSize(16);
    doc.text('Historia Clínica', 20, y);
    y += 10;

    const fields = {
      'Nombre': data.nombre_paciente ?? '-',
      'Edad': data.edad ?? '-',
      'Género': data.genero ?? '-',
      'Fecha de nacimiento': data.fecha_nacimiento ?? '-',
      'Motivo de consulta': data.motivo_consulta ?? '-',
      'Amnesis psiquiátrica': data.amnesis_psiquiatrica ?? '-',
      'Tratamiento': data.tratamiento ?? '-',
      'Plan terapéutico': data.plan_terapeutico ?? '-',
      'Fecha de ingreso': data.fecha_ingreso ?? '-',
    };

    doc.setFontSize(12);
    for (const [label, value] of Object.entries(fields)) {
      doc.text(`${label}: ${value}`, 20, y);
      y += 10;
    }

    // Eventos
    doc.text(`Eventos:`, 20, y);
    y += 8;

    if (Array.isArray(data.eventos) && data.eventos.length > 0) {
      data.eventos.forEach((ev) => {
        const eventoText = `- [${ev.fecha}] ${ev.medico}: ${ev.observacion}`;
        const lines = doc.splitTextToSize(eventoText, 170); // ajusta ancho
        doc.text(lines, 25, y);
        y += lines.length * 8; // espacio por cada línea
      });
    } else {
      doc.text('- Sin eventos registrados.', 25, y);
      y += 10;
    }

    const fileName = `${data.nombre_paciente?.replace(/ /g, '_')}_historia_clinica.pdf`;
    doc.save(fileName);

  } catch (error) {
    console.error("Error al generar PDF:", error);
    alert("No se pudo generar el PDF. Verifica la consola para más detalles.");
  }
}

,
fetchPacientes() {
      fetch("http://127.0.0.1:8000/pacientes/api/pacientes/lista")
        .then(response => response.json())
        .then(data => {
          this.usuarios = data.pacientes;
        })
        .catch(error => {
          console.error("Error al obtener pacientes:", error);
        });
      },
    removePatient(patient) {
      if (confirm(`¿Seguro deseas eliminar a ${patient.nombre_paciente}?`)) {
        fetch(`http://127.0.0.1:8000/pacientes/api/pacientes/detalles/${patient.id}/`, {
          method: "DELETE"
        })
        .then(async response => {
          if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`HTTP ${response.status} - ${errorText}`);
          }
          alert('Paciente eliminado correctamente.');

          // 🔁 Refrescar la lista manualmente SIN redirigir
          this.fetchPacientes();  // 👈 Vuelve a cargar la lista actualizada

          // (opcional) mantener esto si quieres forzar el re-render visual del componente
          this.$router.replace({ path: '/panel', query: { t: Date.now() } });

        })
        .catch(error => {
          console.error("Error al eliminar:", error);
          alert("No se pudo eliminar el paciente.");
        });
      }
    },
    addPatient() {
      this.resetNewPatient();
      this.showModal = true;
    },
    goToSettings() {
      this.$router.push('/ajustes');
    },
    logout() {
      // Limpiar los datos del médico en localStorage
      localStorage.removeItem('medicoId');
      localStorage.removeItem('medicoNombre');
      localStorage.removeItem('medicoPuesto');
      localStorage.removeItem('medicoEmail');

      // Cerrar modal
      this.showProfileModal = false;

      // Redirigir al login
      window.location.href = '/login';
    },
    resetNewPatient() {
  this.newPatient = {
    id: '',
    nombre_paciente: '',
    edad: '',
    genero: '',
    fecha_nacimiento: '',
    motivo_consulta: '',
    amnesis_psiquiatrica: '',
    tratamiento: '',
    plan_terapeutico: '',
    fecha_ingreso: '',
    eventos: []
  };
}
,
  saveNewPatient() {
        fetch("http://localhost:8000/pacientes/api/pacientes/nuevo/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.newPatient)
        })
        .then(async response => {
          if (!response.ok) {
            const errorData = await response.json();
            console.error("Detalles del error del backend:", errorData);
            alert("Error al guardar el paciente:\n" + JSON.stringify(errorData, null, 2));
            throw new Error("Error al guardar el paciente");
          }
          return response.json();
        })
        .then(data => {
          this.usuarios.push(data);
          this.closeModal();
        })
        .catch(error => {
          console.error("Error general:", error);
        });
      },
      buscarPaciente() {
        const nombre = this.searchQuery.trim();
        fetch(`http://localhost:8000/pacientes/api/pacientes/lista/buscar/?nombre=${encodeURIComponent(nombre)}`)
          .then(response => response.json())
          .then(data => {
            this.usuarios = data.pacientes_filtrados || [];
          })
          .catch(error => {
            console.error("Error al buscar pacientes:", error);
          });
  }
},
computed: {
  eventosComoTexto() {
    if (!this.newPatient.eventos || !this.newPatient.eventos.length) return "";
    return this.newPatient.eventos
    .map(ev => `[${ev.fecha}] ${ev.medico}: ${ev.observacion}`)
    .join('\n');
  }
},



      }
    
  

</script>


<style scoped>
.panel-principal {
  min-height: 100vh;
  min-width: 100vw;
  background: linear-gradient(to bottom, #e0f2fe, #f0f9ff);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
}
.header {
  display: flex;
  align-items: center;
  padding: 20px 40px;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  gap: 0;
}
.left-group {
  display: flex;
  align-items: center;
  gap: 24px;
}
.logo-img {
  width: 64px;
  height: 64px;
  object-fit: contain;
  display: block;
}
.search-section {
  display: flex;
  align-items: center;
  gap: 15px;
}
.search-container {
  position: relative;
  width: 280px;
}
.search-container input {
  width: 100%;
  padding: 10px 14px 10px 40px;
  border: none;
  border-radius: 25px;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-size: 15px;
  outline: none;
}
.search-container input::placeholder {
  color: #9CA3AF;
}
.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
}
.add-button {
  width: 28px;
  height: 28px;
  background: #0059af;
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0, 89, 175, 0.18);
  transition: all 0.2s ease;
  margin-left: 100px;
  margin-right: 28px;
  flex-shrink: 0;
}
.add-button:hover {
  background: #003e7e;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 89, 175, 0.25);
}
.user-section {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-left: auto;
}
.user-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-right: 10px;
}
.user-name {
  font-weight: 600;
  color: #374151;
  font-size: 15px;
  line-height: 1.2;
}
.user-role {
  color: #6B7280;
  font-size: 13px;
  font-weight: 400;
  margin-top: 2px;
  line-height: 1.1;
}
.user-avatar {
  width: 40px;
  height: 40px;
  background: #F3F4F6;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #E5E7EB;
  cursor: pointer;
}
.profile-pic {
  width: 40px;
  height: 40px;
  border: 2px solid #e5e7eb;
  background: #f3f4f6;
  border-radius: 50%;
  object-fit: cover;
}
.main-content {
  padding: 40px;
  display: flex;
  justify-content: center;
}
.table-container {
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  width: 100%;
  max-width: 1000px;
}
.table-header {
  display: grid;
  grid-template-columns: 1fr 150px 200px;
  background: #9CA3AF;
  color: white;
  font-weight: 600;
  font-size: 16px;
}
.header-cell {
  padding: 20px 25px;
  text-align: left;
}
.table-body {
  background: white;
}
.table-row {
  display: grid;
  grid-template-columns: 1fr 150px 200px;
  border-bottom: 2px solid #000;
  transition: all 0.2s ease;
}
.table-row:hover {
  background: #f8fafc;
}
.table-row:last-child {
  border-bottom: none;
}
.cell {
  padding: 25px;
  display: flex;
  align-items: center;
  font-size: 16px;
}
.patient-name {
  font-weight: 500;
  color: #374151;
}
.patient-id {
  color: #6B7280;
  font-weight: 500;
}
.actions {
  justify-content: flex-start;
}
.action-button {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 14px;
  color: #374151;
  padding: 8px 12px;
  border-radius: 8px;
  transition: all 0.2s ease;
}
.action-button:hover {
  background: #f3f4f6;
  color: #2563EB;
}
.icon-btn {
  background: none;
  border: none;
  cursor: pointer;
  margin-left: 7px;
  margin-right: 2px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 3px;
  border-radius: 8px;
  transition: background 0.15s;
}
.icon-btn[title]:hover {
  background: #e5e7eb;
}
.action-icon,
.close-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.3);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* --- MODAL historia clínica --- */
.modal {
  background: white;
  border-radius: 14px;
  padding: 32px 28px 24px 28px;
  min-width: 350px;
  width: 600px;
  max-width: 98vw;
  max-height: 85vh;
  box-shadow: 0 8px 32px rgba(0,0,0,0.20);
  display: flex;
  flex-direction: column;
  gap: 18px;
  overflow: hidden;
  position: relative;
}
.modal-scroll {
  overflow-y: auto;
}
.modal-title {
  text-align: center;
  font-size: 1.55rem;
  font-weight: 700;
  color: #0059af;
  margin-top: 0;
  margin-bottom: 10px;
  letter-spacing: 0.5px;
}
.modal label {
  display: flex;
  flex-direction: column;
  font-weight: 500;
  color: #374151;
  gap: 5px;
  margin-bottom: 10px;
}
.modal input,
.modal textarea,
.modal select {
  border: 1.5px solid #ddd;
  border-radius: 8px;
  padding: 8px 10px;
  font-size: 15px;
  outline: none;
  margin-top: 2px;
  transition: border-color 0.2s;
  resize: none;
  background: white;
}
.modal input:focus,
.modal textarea:focus,
.modal select:focus {
  border-color: #0059af;
}
.modal select {
  cursor: pointer;
}
.wide-textarea {
  min-height: 54px;
  resize: vertical;
}
.modal-actions {
  display: flex;
  gap: 14px;
  margin-top: 10px;
  justify-content: flex-end;
}
.modal-save {
  background: #0059af;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 8px 18px;
  font-size: 15px;
  cursor: pointer;
  font-weight: 600;
}
.modal-save:hover {
  background: #003e7e;
}
.modal-cancel {
  background: #e5e7eb;
  color: #374151;
  border: none;
  border-radius: 8px;
  padding: 8px 16px;
  font-size: 15px;
  cursor: pointer;
}
.modal-cancel:hover {
  background: #cfd4db;
}
.modal-close {
  position: absolute;
  top: 16px;
  right: 22px;
  background: none;
  border: none;
  font-size: 2rem;
  color: #aaa;
  cursor: pointer;
  z-index: 10;
  padding: 0 8px;
  line-height: 1;
  transition: color 0.15s;
}
.modal-close:hover {
  color: #0059af;
}

/* --- PANEL DEL PERFIL --- */
.profile-panel-overlay {
  position: fixed;
  inset: 0;
  background: transparent;
  z-index: 2500;
}

.profile-panel {
  position: fixed;
  top: 75px;
  right: 20px;
  width: 200px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
  z-index: 2510;
  padding: 8px;
  animation: slideDown 0.15s cubic-bezier(0.2, 0, 0.2, 1);
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.profile-panel-arrow {
  position: absolute;
  top: -8px;
  right: 12px;
  width: 16px;
  height: 16px;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-bottom: none;
  border-right: none;
  transform: rotate(45deg);
  z-index: 2511;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.profile-options {
  display: flex;
  flex-direction: column;
}

.profile-option {
  display: flex;
  align-items: center;
  padding: 8px;
  border: none;
  background: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.1s;
  text-align: left;
  font-size: 14px;
  color: #050505;
  font-weight: 500;
}

.profile-option:hover {
  background-color: #f2f2f2;
}

.profile-option-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 8px;
  flex-shrink: 0;
}

.settings-icon {
  background-color: #e4e6ea;
  color: #050505;
}

.logout-icon {
  background-color: #e4e6ea;
  color: #050505;
}

.logout-option:hover .logout-icon {
  background-color: #fee;
  color: #e11d48;
}

@media (max-width: 700px) {
  .profile-panel {
    top: 75px;
    right: 10px;
    left: 10px;
    width: auto;
    max-width: calc(100vw - 20px);
  }
  
  .profile-panel-arrow {
    right: 20px;
  }
}
</style>
<template>
  <template>
  <div v-if="paciente">
    <h2>Detalles del Paciente</h2>
    <p><strong>ID:</strong> {{ paciente.id }}</p>
    <p><strong>Nombre:</strong> {{ paciente.nombre_paciente }}</p>
    <!-- Otros campos... -->
  </div>
  <div v-else>
    <p>Cargando datos del paciente...</p>
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
            <input type="text" placeholder="Buscar..." />
          </div>
        </div>
      </div>
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
      <div class="details-container">
        <div class="details-header">
          <h1 class="details-title">HISTORIA CLÍNICA DEL PACIENTE</h1>
        </div>
        
        <div class="details-content">
          <div v-if="patient">
            <div class="detail-row">
              <div class="detail-label">ID:</div>
              <div class="detail-value">{{ patient.id }}</div>
            </div>
            <div class="detail-row">
              <div class="detail-label">Nombre:</div>
              <div class="detail-value">{{ patient.nombre_paciente }}</div>
            </div>
            <div class="detail-row">
              <div class="detail-label">Edad:</div>
              <div class="detail-value">{{ patient.edad }}</div>
            </div>
            <div class="detail-row">
              <div class="detail-label">Género:</div>
              <div class="detail-value">{{ patient.genero }}</div>
            </div>
            <div class="detail-row">
              <div class="detail-label">Fecha de nacimiento:</div>
              <div class="detail-value">{{ patient.fecha_nacimiento }}</div>
            </div>
            <div class="detail-row">
              <div class="detail-label">Motivo de consulta:</div>
              <div class="detail-value">{{ patient.motivo_consulta }}</div>
            </div>
            <div class="detail-row">
              <div class="detail-label">Anamnesis psiquiátrica:</div>
              <div class="detail-value">{{ patient.amnesis_psiquiatrica }}</div>
            </div>
            <div class="detail-row">
              <div class="detail-label">Tratamiento:</div>
              <div class="detail-value">{{ patient.tratamiento }}</div>
            </div>

            <div class="detail-row">
              <div class="detail-label">Plan terapéutico:</div>
              <div class="detail-value">{{ patient.plan_terapeutico }}</div>
            </div>

            <div class="detail-row">
            <div class="detail-label">Fecha de ingreso:</div>
            <div class="detail-value">{{ patient.fecha_ingreso }}</div>
          </div>
          
          <div class="detail-row last-row">
            <div class="detail-label">Eventos:</div>
            <div class="detail-value">
              <template v-if="patient.eventos && patient.eventos.length">
                <ul style="padding-left: 18px;">
                  <li v-for="(evento, idx) in patient.eventos" :key="idx" style="margin-bottom: 8px;">
                    <b>Fecha:</b> {{ evento.fecha }}<br>
                    <b>Médico:</b> {{ evento.medico }}<br>
                    <b>Observación:</b> {{ evento.observacion }}
                  </li>
                </ul>
                </template>
                <template v-else>
                  <span>No hay eventos registrados.</span>
                </template>
              </div>
            </div>

          </div>
          

          <div v-else>
            <p>Cargando datos del paciente...</p>
          </div>

        <!-- Action Buttons -->
        <div class="details-actions">
          <button class="action-btn edit-btn" @click="editPatient">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" 
                stroke="#0059af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Editar
          </button>
          <button class="action-btn delete-btn" @click="deletePatient">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
              <path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2m2 0v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6m3 6v6m4-6v6m4-6v6"
                stroke="#e11d48" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Eliminar
          </button>
          <button class="action-btn back-btn" @click="goBack">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
              <path d="M19 12H5M12 19l-7-7 7-7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Volver a la lista
          </button>
        </div>
      </div>
    </div>

    <!-- MODAL de editar historia clínica -->
    <div v-if="showEditModal" class="modal-overlay">
      <div class="modal modal-scroll">
        <button class="modal-close" @click="closeEditModal" title="Cerrar">
          &times;
        </button>
        <h2 class="modal-title">Editar historia clínica</h2>
        <form @submit.prevent="saveEditedPatient">
          <label>
            ID:
            <input v-model="editedPatient.id" />
          </label>
          <label>
            Nombre del paciente:
            <input v-model="editedPatient.nombre_paciente" />
          </label>
          <label>
            Edad:
            <input v-model="editedPatient.edad" />
          </label>
          <label>
            <label>
              Género:
              <select v-model="editedPatient.genero" required>
                <option value="">Selecciona una opción</option>
                <option value="femenino">Femenino</option>
                <option value="masculino">Masculino</option>
                <option value="otro">Otro</option>
              </select>
            </label>
          </label>
          <label>
            Fecha de nacimiento:
            <input type="date" v-model="editedPatient.fecha_nacimiento" />
          </label>
          <label>
            Motivo de consulta:
            <textarea v-model="editedPatient.motivo_consulta" />
          </label>
          <label>
            Amnamnesis psiquiátrica:
            <textarea v-model="editedPatient.amnesis_psiquiatrica" />
          </label>
          <label>
            Tratamiento:
            <textarea v-model="editedPatient.tratamiento" />
          </label>
          <label>
            Plan terapéutico:
            <textarea v-model="editedPatient.plan_terapeutico" />
          </label>
          <label v-if="editedPatient.fecha_ingreso">
            Fecha de ingreso:
            <input type="date" v-model="editedPatient.fecha_ingreso" />
          </label>

          <label v-if="editedPatient.eventos">
            Eventos:
            <div v-if="editedPatient.eventos && editedPatient.eventos.length">
              <ul style="padding-left: 16px;">
                <li v-for="(evento, i) in editedPatient.eventos" :key="i">
                  <b>Fecha:</b> {{ evento.fecha }}<br>
                  <b>Médico:</b> {{ evento.medico }}<br>
                  <b>Observación:</b> {{ evento.observacion }}
                </li>
              </ul>
            </div>
            <div v-else>
              <span style="color:#666;">No hay eventos registrados.</span>
            </div>
            <!-- Botón para abrir el modal de agregar evento -->
             <button type="button" class="modal-save" @click="abrirModalEvento" style="width:100%;margin-top:12px;">
              Agregar evento
            </button>
          </label>

          <div class="modal-actions">
            <button type="submit" class="modal-save">Guardar cambios</button>
            <button type="button" class="modal-cancel" @click="closeEditModal">Cancelar</button>
          </div>
        </form>
      </div>
    </div>
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


    <!-- PANEL DE PERFIL simplificado -->
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
  </div>
</template>

<script>
export default {
  name: 'VerDetalles',
  data() {
    return {
      showProfileModal: false,
      showEditModal: false,
      userName: 'Nombre completo médico',
      userRole: 'Puesto del médico',
      patient: null,
      showEventModal: false,
      newEvent: {
        fecha: '',
        medico: '',
        observacion: ''
      },
      editedPatient: {
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
      }
    }
  },
    mounted() {
          this.userName = localStorage.getItem('medicoNombre') || 'Nombre no disponible';
          this.userRole = localStorage.getItem('medicoPuesto') || 'Rol no disponible';
          const id = this.$route.params.id;
          fetch(`http://127.0.0.1:8000/pacientes/api/pacientes/detalles/${id}/`)
            .then(response => response.json())
            .then(data => {
              console.log("📦 Datos del paciente:", data);
              this.patient = data;


              // Mapeo manual de backend → frontend
              this.editedPatient = {
                id: data.id,
                nombre_paciente: data.nombre_paciente,
                edad: data.edad,
                genero: data.genero,
                fecha_nacimiento: data.fecha_nacimiento,
                motivo_consulta: data.motivo_consulta,
                amnesis_psiquiatrica: data.amnesis_psiquiatrica,
                tratamiento: data.tratamiento,
                plan_terapeutico: data.plan_terapeutico,
                fecha_ingreso: data.fecha_ingreso,
                eventos: data.eventos
              };

            })
            .catch(error => {
              console.error("Error al obtener detalles del paciente:", error);
            });
        }

,

  methods: {
    goToPanel() {
      this.$router.push('/panel');
    },
    
    editPatient() {
      let eventosArray = [];
      if (Array.isArray(this.patient.eventos)) {
        eventosArray = this.patient.eventos;
      } else if (typeof this.patient.eventos === 'string') {
        try {
          eventosArray = JSON.parse(this.patient.eventos) || [];
        } catch {
          eventosArray = [];
        }
      }
      this.editedPatient = {
        id: this.patient.id,
        nombre_paciente: this.patient.nombre_paciente,
        edad: this.patient.edad,
        genero: this.patient.genero,
        fecha_nacimiento: this.patient.fecha_nacimiento,
        motivo_consulta: this.patient.motivo_consulta,
        amnesis_psiquiatrica: this.patient.amnesis_psiquiatrica,
        tratamiento: this.patient.tratamiento,
        plan_terapeutico: this.patient.plan_terapeutico,
        fecha_ingreso: this.patient.fecha_ingreso || '',
        eventos: eventosArray
      };
    // Removed misplaced line causing syntax error

        this.showEditModal = true;
      },
    closeEditModal() {
      this.showEditModal = false;
    },
    saveEditedPatient() {
      const id = this.editedPatient.id;
      const payload = {
        id: id,
        nombre_paciente: this.editedPatient.nombre_paciente,
        edad: this.editedPatient.edad,
        genero: this.editedPatient.genero,
        fecha_nacimiento: this.editedPatient.fecha_nacimiento,
        motivo_consulta: this.editedPatient.motivo_consulta,
        amnesis_psiquiatrica: this.editedPatient.amnesis_psiquiatrica,
        tratamiento: this.editedPatient.tratamiento,
        plan_terapeutico: this.editedPatient.plan_terapeutico,
        fecha_ingreso: this.editedPatient.fecha_ingreso || new Date().toISOString().split('T')[0],
        eventos: this.editedPatient.eventos   
      };
    

        fetch(`http://127.0.0.1:8000/pacientes/api/pacientes/detalles/${id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(payload)
        })
        .then(response => {
          if (!response.ok) throw new Error("Error al actualizar los datos");
          return response.json();
        })
        .then(data => {
          this.patient = data;
          this.closeEditModal();
          alert('Historia clínica actualizada correctamente');
        })
        .catch(error => {
          console.error("Error al actualizar:", error);
          alert("No se pudo actualizar el paciente.");
        });
      },
    deletePatient() {
        if (confirm(`¿Seguro deseas eliminar a ${this.patient.nombre_paciente}?`)) {
          fetch(`http://127.0.0.1:8000/pacientes/api/pacientes/detalles/${this.patient.id}/`, {
            method: "DELETE"
          })
          .then(response => {
            if (!response.ok) throw new Error("Error al eliminar el paciente");
            alert('Paciente eliminado. Redirigiendo a la lista...');
            this.$router.push('/panel');
          })
          .catch(error => {
            console.error("Error al eliminar:", error);
            alert("No se pudo eliminar el paciente.");
          });
        }
      },
    goBack() {
      alert('Volver a la lista de pacientes (aquí implementar navegación)');
      this.$router.push('/panel');
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
    abrirModalEvento() {
      this.newEvent = { fecha: '', medico: '', observacion: '' }
      this.showEventModal = true;
    },
    cerrarModalEvento() {
      this.showEventModal = false;
    },
    guardarEvento() {
      if (typeof this.editedPatient.eventos === 'string') {
        try {
          this.editedPatient.eventos = JSON.parse(this.editedPatient.eventos) || [];
        } catch {
          this.editedPatient.eventos = [];
        }
      }
      if (!this.newEvent.fecha || !this.newEvent.medico || !this.newEvent.observacion) {
        alert('Completa todos los campos del evento');
        return;
  }
  this.editedPatient.eventos.push({ ...this.newEvent });
  this.showEventModal = false;
},
eventosComoTexto() {
  if (!Array.isArray(this.editedPatient.eventos)) return '';
  return this.editedPatient.eventos.map(ev => `[${ev.fecha}] ${ev.medico}: ${ev.observacion}`).join('\n');
},
}

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

.details-container {
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  width: 100%;
  max-width: 800px;
}

.details-header {
  background: #9ca3af;
  padding: 32px 40px 24px 40px;
  border-bottom: 1px solid #e5e7eb;
}

.details-title {
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  color: white;
  margin: 0;
  letter-spacing: 0.5px;
  text-transform: capitalize;
}

.details-content {
  padding: 32px 40px;
}

.detail-row {
  display: flex;
  align-items: flex-start;
  padding: 16px 40px;
  margin: 0 -40px;
  border-bottom: 3px solid #374151;
  min-height: 56px;
}

.detail-row.last-row {
  border-bottom: none;
}

.detail-label {
  width: 200px;
  font-weight: 500;
  color: #374151;
  font-size: 16px;
  flex-shrink: 0;
  padding-right: 24px;
}

.detail-value {
  flex: 1;
  color: #6B7280;
  font-size: 16px;
  line-height: 1.5;
}

.details-actions {
  background: #f8fafc;
  padding: 24px 40px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid;
}

.edit-btn {
  background: white;
  color: #0059af;
  border-color: #0059af;
}

.edit-btn:hover {
  background: #f0f8ff;
}

.delete-btn {
  background: white;
  color: #e11d48;
  border-color: #e11d48;
}

.delete-btn:hover {
  background: #fef2f2;
}

.back-btn {
  background: #0059af;
  color: white;
  border-color: #0059af;
}

.back-btn:hover {
  background: #003e7e;
}

/* --- MODAL de editar historia clínica --- */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.3);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}

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
}

.modal input:focus,
.modal textarea:focus,
.modal select:focus {
  border-color: #0059af;
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

/* --- PANEL DEL PERFIL simplificado --- */
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
  
  .details-container {
    margin: 0 10px;
  }
  
  .details-header,
  .details-content,
  .details-actions {
    padding-left: 20px;
    padding-right: 20px;
  }
  
  .detail-label {
    width: 140px;
    font-size: 14px;
  }
  
  .detail-value {
    font-size: 14px;
  }
  
  .details-actions {
    flex-direction: column;
    gap: 8px;
  }
  
  .action-btn {
    justify-content: center;
  }
}
</style>

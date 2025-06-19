<template>
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
            <input type="text" placeholder="Buscar..." disabled />
          </div>
        </div>
      </div>
      <div class="user-section">
        <div class="user-info">
          <span class="user-name">{{ userName }}</span>
          <span class="user-role">{{ userRole }}</span>
        </div>
        <div class="user-avatar" @click="showProfileModal = true" style="cursor:pointer" title="Ver perfil">
          <img src="@/assets/perfil.png" alt="Avatar" class="profile-pic" />
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content ajustes-main-content">
      <div class="ajustes-card">
        <div class="ajustes-gear">
          
          <svg width="64" height="64" viewBox="0 0 64 64" fill="none">
            <g>
              <circle cx="32" cy="32" r="10" fill="#fff" stroke="#2653a5" stroke-width="2"/>
              <path stroke="#2653a5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                d="M32 14V8M32 56v-6M50 32h6M8 32h6
                  M46.6 46.6l4.2 4.2M13.2 13.2l4.2 4.2
                  M46.6 17.4l4.2-4.2M13.2 50.8l4.2-4.2
                  M32 24a8 8 0 1 1 0 16a8 8 0 0 1 0-16Z"
              />
            </g>
          </svg>
        </div>
        <h2 class="ajustes-title">Ajustes de la cuenta</h2>
        <button class="ajustes-btn ajustes-btn-blue" @click="openModal('perfil')">
          <svg width="24" height="24" fill="none" stroke="white" stroke-width="2" viewBox="0 0 24 24">
            <path d="M15.232 5.232l3.536 3.536M4 20h4l11-11a2.5 2.5 0 0 0-3.536-3.536L4 16v4z"/>
          </svg>
          Editar perfil
        </button>
        <button class="ajustes-btn ajustes-btn-gray" @click="openModal('password')">
          <svg width="24" height="24" fill="none" stroke="#374151" stroke-width="2" viewBox="0 0 24 24">
            <rect x="6" y="11" width="12" height="8" rx="2"/>
            <path d="M8 11V7a4 4 0 0 1 8 0v4"/>
          </svg>
          Cambiar contraseña
        </button>
        <button class="ajustes-btn ajustes-btn-blue" @click="openModal('soporte')">
          <svg width="24" height="24" fill="none" stroke="white" stroke-width="2" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10"/>
            <circle cx="12" cy="17" r="1"/>
            <path d="M12 7v4"/>
          </svg>
          Ayuda y soporte
        </button>
      </div>
    </div>

    <!-- MODAL Editar Perfil -->
    <div v-if="modal === 'perfil'" class="modal-overlay">
      <div class="modal">
        <button class="modal-close" @click="closeModal">&times;</button>
        <h2 class="modal-title">Editar perfil</h2>
        <form @submit.prevent="saveProfile">
          <label>
            Nombre completo:
            <input v-model="editName" type="text" required />
          </label>
          <label>
            Correo electrónico:
            <input v-model="editEmail" type="email" required />
          </label>
          <div class="modal-actions">
            <button type="submit" class="modal-save">Guardar</button>
            <button type="button" class="modal-cancel" @click="closeModal">Cancelar</button>
          </div>
        </form>
      </div>
    </div>
    <!-- MODAL Cambiar contraseña -->
    <div v-if="modal === 'password'" class="modal-overlay">
      <div class="modal">
        <button class="modal-close" @click="closeModal">&times;</button>
        <h2 class="modal-title">Cambiar contraseña</h2>
        <form @submit.prevent="savePassword">
          <label>
            Contraseña actual:
            <input v-model="oldPassword" type="password" required autocomplete="current-password" />
          </label>
          <label>
            Nueva contraseña:
            <input v-model="newPassword" type="password" required autocomplete="new-password" />
          </label>
          <label>
            Confirmar nueva contraseña:
            <input v-model="confirmPassword" type="password" required autocomplete="new-password" />
          </label>
          <div class="modal-actions">
            <button type="submit" class="modal-save">Cambiar</button>
            <button type="button" class="modal-cancel" @click="closeModal">Cancelar</button>
          </div>
        </form>
      </div>
    </div>
    <!-- MODAL Soporte -->
    <div v-if="modal === 'soporte'" class="modal-overlay">
      <div class="modal">
        <button class="modal-close" @click="closeModal">&times;</button>
        <h2 class="modal-title">Ayuda y soporte</h2>
        <div class="soporte-info">
          <p>
            <strong>Correo:</strong> <a href="mailto:soporte@mindsecure.com">soporte@mindsecure.com</a>
          </p>
          <p>
            <strong>Teléfono:</strong> <a href="tel:+573012345678">+57 301 234 5678</a>
          </p>
        </div>
        <div class="modal-actions" style="justify-content: flex-end;">
          <button type="button" class="modal-save" @click="closeModal">Cerrar</button>
        </div>
      </div>
    </div>

    <!-- PANEL DE PERFIL -->
    <div v-if="showProfileModal">
      <div class="profile-panel-overlay" @click.self="showProfileModal = false"></div>
      <div class="profile-panel">
        <div class="profile-panel-arrow"></div>
        <div class="profile-options">
          <button class="profile-option" @click="openModal('perfil'); showProfileModal = false;">
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

<script setup>
import { ref } from 'vue'
import axios from 'axios';
const showProfileModal = ref(false);
const modal = ref(null);

// Estado para datos de ejemplo
const userName = ref(localStorage.getItem('medicoNombre') || 'Nombre no disponible');
const userRole = ref(localStorage.getItem('medicoPuesto') || 'Rol no disponible');
const editName = ref(userName.value);
const editEmail = ref("medico@mindsecure.com");
const oldPassword = ref("");
const newPassword = ref("");
const confirmPassword = ref("");

// Abrir modal según tipo
function openModal(type) {
  modal.value = type;

  if (type === 'perfil') {
    editName.value = localStorage.getItem('medicoNombre') || '';
    editEmail.value = localStorage.getItem('medicoEmail') || ''; // si no tienes email, puedes dejarlo fijo
  }

  if (type === 'password') {
    oldPassword.value = "";
    newPassword.value = "";
    confirmPassword.value = "";
  }
}
function closeModal() {
  modal.value = null;
}


// Acciones ejemplo 
async function saveProfile() {
    const medicoId = localStorage.getItem('medicoId');

    try {
      const response = await axios.post('http://127.0.0.1:8000/medicos/api/editar-perfil-medico/', {
        id: medicoId,
        nombre: editName.value,
        email: editEmail.value
      });

      userName.value = editName.value;
      localStorage.setItem('medicoNombre', editName.value);
      localStorage.setItem('medicoEmail', editEmail.value);

      alert(response.data.mensaje || "Perfil actualizado exitosamente.");
      closeModal();
    } catch (error) {
      console.error("Error al guardar el perfil:", error);
      alert("No se pudo actualizar el perfil.");
    }
  }

async function savePassword() {
    const medicoId = localStorage.getItem('medicoId');
    console.log("ID médico:", medicoId);

    if (newPassword.value !== confirmPassword.value) {
      alert("Las contraseñas no coinciden");
      return;
    }

    try {
      await axios.post('http://127.0.0.1:8000/medicos/api/cambiar-clave-medico/', {
      id: medicoId,
      clave_actual: oldPassword.value,
      nueva_clave: newPassword.value,
      confirmar_clave: confirmPassword.value
    });


      alert("Contraseña cambiada exitosamente.");
      closeModal();
    } catch (error) {
      console.log("Respuesta del backend:", error.response?.data);

      if (error.response && error.response.data) {
        alert(error.response.data.error || error.response.data.non_field_errors?.[0] || "Error al cambiar la contraseña.");
      } else {
        alert("Error desconocido al cambiar la contraseña.");
      }
      console.error("Error al cambiar contraseña:", error);
    }
  }

function logout() {
  showProfileModal.value = false;

  // Borra los datos de sesión
  localStorage.removeItem('medicoId');
  localStorage.removeItem('medicoNombre');
  localStorage.removeItem('medicoPuesto');
  localStorage.removeItem('medicoEmail');

  // Redirige al login
  window.location.href = '/login';
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap');

.panel-principal {
  min-height: 100vh;
  min-width: 100vw;
  background: linear-gradient(to bottom, #e0f2fe, #f0f9ff);
  font-family: 'Segoe UI', Arial, sans-serif;
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
  .left-group {
    display: flex;
    align-items: center;
    gap: 24px;
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
      .search-container {
        position: relative;
        width: 250px;
        input {
          width: 100%;
          padding: 10px 14px 10px 40px;
          border: none;
          border-radius: 25px;
          background: white;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
          font-size: 15px;
          outline: none;
        }
        input::placeholder {
          color: #9CA3AF;
        }
        .search-icon {
          position: absolute;
          left: 12px;
          top: 50%;
          transform: translateY(-50%);
        }
      }
    }
  }
  .user-section {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-left: auto;
    .user-info {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      margin-right: 10px;
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
      .profile-pic {
        width: 40px;
        height: 40px;
        border: 2px solid #e5e7eb;
        background: #f3f4f6;
        border-radius: 50%;
        object-fit: cover;
      }
    }
  }
}

.ajustes-main-content {
  padding: 40px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: 74vh;
}

.ajustes-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  min-width: 360px;
  max-width: 400px;
  width: 100%;
  padding: 48px 32px 36px 32px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 22px;
  .ajustes-gear {
    margin-bottom: 5px;
    svg { display: block; margin: 0 auto;}
  }
  .ajustes-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #233a62;
    margin-bottom: 6px;
    margin-top: 8px;
    text-align: center;
    letter-spacing: 0.2px;
  }
  .ajustes-btn {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 15px 20px;
    font-size: 1.09rem;
    font-weight: bold;
    border-radius: 18px;
    border: none;
    outline: none;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px 0 rgba(0,0,0,0.05);
    cursor: pointer;
    transition: background 0.18s, color 0.18s;
    svg {
      flex-shrink: 0;
    }
    &:last-child { margin-bottom: 0; }
  }
  .ajustes-btn-blue {
    background: #2653a5;
    color: #fff;
    &:hover { background: #17396c; }
    svg { stroke: #fff !important; }
  }
  .ajustes-btn-gray {
    background: #e1e2e7;
    color: #374151;
    &:hover { background: #c5c6cb; }
    svg { stroke: #374151 !important; }
  }
}

/* --- MODALES --- */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.18);
  z-index: 2100;
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal {
  background: white;
  border-radius: 14px;
  padding: 36px 28px 22px 28px;
  min-width: 320px;
  width: 410px;
  max-width: 95vw;
  max-height: 92vh;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
  display: flex;
  flex-direction: column;
  gap: 15px;
  overflow: hidden;
  position: relative;
}
.modal-title {
  text-align: center;
  font-size: 1.2rem;
  font-weight: 700;
  color: #2653a5;
  margin-top: 0;
  margin-bottom: 8px;
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
.modal input {
  border: 1.5px solid #ddd;
  border-radius: 8px;
  padding: 8px 10px;
  font-size: 15px;
  outline: none;
  margin-top: 2px;
  transition: border-color 0.2s;
}
.modal input:focus {
  border-color: #2653a5;
}
.modal-actions {
  display: flex;
  gap: 14px;
  margin-top: 10px;
  justify-content: flex-end;
}
.modal-save {
  background: #2653a5;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 8px 18px;
  font-size: 15px;
  cursor: pointer;
  font-weight: 600;
}
.modal-save:hover {
  background: #17396c;
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
  top: 14px;
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
  color: #2653a5;
}
.soporte-info {
  padding: 20px 0;
  font-size: 1.09rem;
  color: #2653a5;
  p {
    margin: 8px 0;
  }
  a {
    color: #2653a5;
    text-decoration: underline;
  }
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
  .header {
    padding: 12px 12px;
    .left-group {
      .logo-img {
        width: 42px;
        height: 42px;
      }
      .search-container {
        width: 110px;
        input {
          font-size: 13px;
        }
      }
    }
    .user-info {
      .user-name { font-size: 13px;}
      .user-role { font-size: 12px;}
    }
    .user-avatar, .profile-pic {
      width: 32px !important;
      height: 32px !important;
    }
  }
  .ajustes-main-content {
    padding: 15px;
  }
  .ajustes-card {
    padding: 28px 8px 18px 8px;
    min-width: 95vw;
    .ajustes-title {
      font-size: 1.01rem;
    }
  }
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
  .modal {
    min-width: 98vw;
    width: 98vw;
    padding: 18px 5vw 12px 5vw;
  }
}
</style>
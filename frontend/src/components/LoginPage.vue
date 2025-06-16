<template>
  <div class="login-container">
    <!-- Imagen de fondo -->
    <div class="background-image"></div>
    
    <!-- Contenido principal -->
    <div class="login-content">
      <!-- Logo -->
      <div class="logo-container">
        <img src="@/assets/logomindsecure.png" alt="MindSecure" class="logo" />
      </div>
      
      <!-- Formulario de login -->
      <div class="login-form">
        <!-- Campo ID -->
        <div class="input-group">
          <div class="input-container">
            <svg class="input-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <input 
              type="text" 
              placeholder="ID" 
              class="login-input"
              v-model="loginForm.id"
            />
          </div>
        </div>
        
        <!-- Campo contraseña -->
        <div class="input-group">
          <div class="input-container">
            <svg class="input-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2" stroke="currentColor" stroke-width="2"/>
              <circle cx="12" cy="16" r="1" fill="currentColor"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <input 
              :type="showPassword ? 'text' : 'password'"
              placeholder="Contraseña" 
              class="login-input"
              v-model="loginForm.password"
            />
            <button 
              type="button" 
              class="password-toggle"
              @click="togglePassword"
            >
              <svg v-if="!showPassword" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" stroke="currentColor" stroke-width="2"/>
                <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/>
              </svg>
              <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" stroke="currentColor" stroke-width="2"/>
                <line x1="1" y1="1" x2="23" y2="23" stroke="currentColor" stroke-width="2"/>
              </svg>
            </button>
          </div>
        </div>
        
        <!-- Enlace de contraseña olvidada -->
        <div class="forgot-password-section">
          <a href="#" class="forgot-password-link" @click.prevent="goToForgotPassword">
            ¿Olvidaste tu contraseña?
          </a>
        </div>
        
        <!-- Botón de login -->
        <button 
          class="login-button"
          @click="handleLogin"
          :disabled="isLoading"
        >
          <span v-if="!isLoading">Ingresar</span>
          <div v-else class="loading-spinner"></div>
        </button>
        
        <!-- Enlace de ayuda -->
        <div class="help-section">
          <a href="#" class="help-link" @click.prevent="goToHelp">
            ¿Necesitas ayuda?
          </a>
        </div>
      </div>
    </div>

    <!-- MODAL: Olvidaste tu contraseña -->
    <div v-if="showForgotPasswordModal" class="modal-overlay">
      <div class="modal-content">
        <button class="modal-close" @click="showForgotPasswordModal = false">&times;</button>
        <h2 class="modal-title">¿Olvidaste tu contraseña?</h2>
        <div v-if="forgotPasswordSent" class="modal-message modal-success">
          Si tu correo está registrado, te hemos enviado instrucciones para restablecer tu contraseña.
        </div>
        <form v-else @submit.prevent="handleForgotPassword">
          <input
            type="email"
            v-model="forgotPasswordEmail"
            required
            placeholder="Tu correo electrónico"
            class="modal-input"
          />
          <button class="modal-action-button" type="submit">Enviar instrucciones</button>
        </form>
      </div>
    </div>

    <!-- MODAL: Necesitas ayuda -->
    <div v-if="showHelpModal" class="modal-overlay">
      <div class="modal-content">
        <button class="modal-close" @click="showHelpModal = false">&times;</button>
        <h2 class="modal-title">Soporte MindSecure</h2>
        <div class="modal-message">
          <strong>Correo:</strong> soporte@mindsecure.com <br>
          <strong>Teléfono:</strong> +57 301 234 5678
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      loginForm: {
        id: '',
        password: ''
      },
      showPassword: false,
      isLoading: false,
      // MODALES
      showForgotPasswordModal: false,
      showHelpModal: false,
      forgotPasswordEmail: '',
      forgotPasswordSent: false
    };
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    async handleLogin() {
        this.isLoading = true;
        try {
          const response = await axios.post('http://127.0.0.1:8000/', {
            id: this.loginForm.id,
            clave_acceso: this.loginForm.password
          });

          const medico = response.data.medico;

          console.log('Login exitoso:', medico);
          alert('Bienvenido Dr. ' + medico.nombre);

          // 🔐 Guardar los datos en localStorage
          localStorage.setItem('medicoNombre', response.data.medico.nombre);
          localStorage.setItem('medicoPuesto', response.data.medico.puesto);
          localStorage.setItem('medicoId', response.data.medico.id);
          localStorage.setItem('medicoEmail', response.data.medico.email);  

          
          // Redirigir al panel
          this.$router.push('/panel');

        } catch (error) {
          if (error.response?.data?.error) {
            alert('Error: ' + error.response.data.error);
          } else {
            alert('Error desconocido al iniciar sesión');
          }
        } finally {
          this.isLoading = false;
        }
      },
    goToForgotPassword() {
      this.showForgotPasswordModal = true;
      this.forgotPasswordSent = false;
      this.forgotPasswordEmail = '';
    },
    goToHelp() {
      this.showHelpModal = true;
    },
    handleForgotPassword() {
      this.forgotPasswordSent = true;
      // Aquí agregar backend
      setTimeout(() => {
        this.showForgotPasswordModal = false;
      }, 2500);
    }
  }
};
</script>

<style scoped>
.login-container {
  position: relative;
  min-height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  margin: 0;
  padding: 0;
}

.background-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/bg.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  z-index: -2;
}

.background-image::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(1px);
  z-index: -1;
}

.login-content {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 400px;
  width: 100%;
  padding: 0 20px;
}

.logo-container {
  margin-bottom: 60px;
}

.logo {
  max-width: 280px;
  height: auto;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

.login-form {
  width: 100%;
  max-width: 350px;
}

.input-group {
  margin-bottom: 20px;
}

.input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 16px;
  width: 20px;
  height: 20px;
  color: #4A90E2;
  z-index: 1;
}

.login-input {
  width: 100%;
  padding: 16px 16px 16px 50px;
  border: none;
  border-radius: 25px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  font-size: 16px;
  color: #333;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  outline: none;
}

.login-input:focus {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 6px 20px rgba(74, 144, 226, 0.3);
  transform: translateY(-2px);
}

.login-input::placeholder {
  color: #888;
  font-weight: 400;
}

.password-toggle {
  position: absolute;
  right: 16px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  border-radius: 50%;
  transition: background-color 0.2s ease;
}

.password-toggle:hover {
  background-color: rgba(74, 144, 226, 0.1);
}

.password-toggle svg {
  width: 20px;
  height: 20px;
  color: #4A90E2;
}

.forgot-password-section {
  text-align: right;
  margin-bottom: 20px;
}

.forgot-password-link {
  color: #4A90E2;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  display: inline-block;
}

.forgot-password-link:hover {
  color: #357ABD;
  text-decoration: underline;
  transform: translateX(-2px);
}

.login-button {
  width: 100%;
  padding: 16px;
  background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%);
  color: white;
  border: none;
  border-radius: 25px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(74, 144, 226, 0.4);
  margin-top: 10px;
  min-height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.login-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(74, 144, 226, 0.5);
}

.login-button:active:not(:disabled) {
  transform: translateY(0);
}

.login-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.loading-spinner {
  width: 24px;
  height: 24px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.help-section {
  text-align: center;
  margin-top: 30px;
}

.help-link {
  color: #4A90E2;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: color 0.3s ease;
}

.help-link:hover {
  color: #357ABD;
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 480px) {
  .login-content {
    padding: 0 15px;
  }
  
  .logo {
    max-width: 240px;
  }
  
  .login-form {
    max-width: 320px;
  }
  
  .login-input {
    font-size: 16px; /* Previene zoom en iOS */
  }
  
  .forgot-password-section {
    text-align: center;
  }
}

@media (max-height: 700px) {
  .logo-container {
    margin-bottom: 40px;
  }
  
  .logo {
    max-width: 220px;
  }
}

/* Animaciones de entrada */
.login-content {
  animation: fadeInUp 0.8s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.input-group {
  animation: fadeInUp 0.8s ease-out;
  animation-fill-mode: both;
}

.input-group:nth-child(1) { animation-delay: 0.1s; }
.input-group:nth-child(2) { animation-delay: 0.2s; }
.forgot-password-section { 
  animation: fadeInUp 0.8s ease-out 0.25s both;
}
.login-button { 
  animation: fadeInUp 0.8s ease-out 0.3s both;
}
.help-section { 
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

/* MODALES */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(33, 50, 80, 0.18);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
  animation: fadeIn 0.25s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-content {
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 6px 32px rgba(44, 90, 155, 0.25);
  padding: 38px 24px 32px 24px;
  width: 100%;
  max-width: 360px;
  position: relative;
  animation: fadeModalUp 0.3s;
}

@keyframes fadeModalUp {
  from { opacity: 0; transform: translateY(30px);}
  to { opacity: 1; transform: translateY(0);}
}

.modal-title {
  font-size: 1.35rem;
  font-weight: 700;
  color: #1b365d;
  text-align: center;
  margin-bottom: 1.1rem;
}

.modal-close {
  position: absolute;
  right: 16px;
  top: 16px;
  background: none;
  border: none;
  font-size: 2rem;
  color: #789;
  cursor: pointer;
  transition: color 0.2s;
}

.modal-close:hover { color: #357ABD; }

.modal-message {
  font-size: 1rem;
  color: #28477d;
  margin-bottom: 1.1rem;
  text-align: center;
  line-height: 1.5;
}

.modal-success {
  color: #21994d;
  font-weight: 600;
  background: #e6faee;
  border-radius: 12px;
  padding: 1rem;
}

.modal-input, .modal-action-button {
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

/* input del modal */
.modal-input {
  padding: 12px 16px;
  font-size: 1rem;
  margin-bottom: 1rem;
  border-radius: 12px;
  border: 1px solid #c6d4e7;
  background: #f5f9fc;
  outline: none;
  transition: border-color 0.2s;
}

.modal-input:focus {
  border-color: #357ABD;
  background: #fff;
}

/* botón del modal */
.modal-action-button {
  padding: 12px 0;
  border-radius: 12px;
  background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%);
  color: #fff;
  font-weight: 600;
  font-size: 1.07rem;
  border: none;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
  box-shadow: 0 4px 16px rgba(74, 144, 226, 0.20);
}

.modal-action-button:hover {
  background: linear-gradient(135deg, #357ABD 0%, #4A90E2 100%);
  transform: translateY(-2px);
}

/* Responsive modal */
@media (max-width: 540px) {
  .modal-content {
    padding: 26px 10px 18px 10px;
    max-width: 98vw;
  }
}
</style>

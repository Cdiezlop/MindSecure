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
        
        <!-- Campo Contraseña -->
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
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      loginForm: {
        id: '',
        password: ''
      },
      showPassword: false,
      isLoading: false
    }
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    
    handleLogin() {
      this.isLoading = true;
      
      // Espacio para la lógica real
      console.log('Login attempt:', this.loginForm);
      
      // Simular delay
      setTimeout(() => {
        this.isLoading = false;
        // Aquí manejarías la respuesta del login
      }, 2000);
    },
    
    goToHelp() {
      // Lógica para ir a la página de ayuda
      console.log('Going to help page');
    }
  }
}
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
.login-button { 
  animation: fadeInUp 0.8s ease-out 0.3s both;
}
.help-section { 
  animation: fadeInUp 0.8s ease-out 0.4s both;
}
</style>

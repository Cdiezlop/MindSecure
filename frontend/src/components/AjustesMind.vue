<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-slate-100 to-blue-100">
    <!-- Header con logo -->
    <div class="flex items-center justify-between p-6 bg-white/80 backdrop-blur-sm shadow-sm">
      <div class="flex items-center gap-3">
        <img src="@/assets/cerebro.png" alt="MIND-SECURE" class="w-12 h-12" />
        <div>
          <h1 class="text-2xl font-bold text-gray-800">MIND-SECURE</h1>
          <p class="text-sm text-gray-600">Configuración de cuenta</p>
        </div>
      </div>
      <div class="text-right">
        <p class="text-sm font-medium text-gray-800">Nombre completo médico</p>
        <p class="text-xs text-gray-500">Puesto del médico</p>
      </div>
    </div>

    <!-- Contenido principal -->
    <div class="flex flex-col items-center justify-center p-8">
      <div class="bg-white/90 backdrop-blur-sm rounded-3xl shadow-2xl p-10 w-full max-w-lg border border-white/20">
        <div class="text-center mb-8">
          <div class="w-20 h-20 bg-gradient-to-br from-blue-500 to-blue-600 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
            </svg>
          </div>
          <h2 class="text-3xl font-bold text-gray-800 mb-2">Ajustes de la cuenta</h2>
          <p class="text-gray-600">Personaliza tu experiencia médica</p>
        </div>
        
        <div class="flex flex-col gap-4">
          <!-- Botón Editar Perfil -->
          <button
            @click="modalEditarPerfil = true"
            class="group flex items-center gap-4 px-6 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-2xl shadow-lg hover:shadow-xl hover:from-blue-700 hover:to-blue-800 transition-all duration-300 transform hover:scale-105"
          >
            <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center group-hover:bg-white/30 transition-all">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536M9 11l3.536-3.536a2 2 0 112.828 2.828L11 13.828M7 17h3.586a1 1 0 00.707-.293l7.414-7.414a4 4 0 00-5.656-5.657l-7.415 7.415a1 1 0 00-.293.707V17a1 1 0 001 1z"></path>
              </svg>
            </div>
            <div class="flex-1 text-left">
              <h3 class="font-semibold text-lg">Editar perfil</h3>
              <p class="text-blue-100 text-sm">Actualiza tu información personal</p>
            </div>
            <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path>
            </svg>
          </button>

          <!-- Botón Cambiar Contraseña -->
          <button
            @click="modalCambiarContrasena = true"
            class="group flex items-center gap-4 px-6 py-4 bg-gradient-to-r from-slate-600 to-slate-700 text-white rounded-2xl shadow-lg hover:shadow-xl hover:from-slate-700 hover:to-slate-800 transition-all duration-300 transform hover:scale-105"
          >
            <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center group-hover:bg-white/30 transition-all">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
              </svg>
            </div>
            <div class="flex-1 text-left">
              <h3 class="font-semibold text-lg">Cambiar contraseña</h3>
              <p class="text-slate-100 text-sm">Mantén tu cuenta segura</p>
            </div>
            <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path>
            </svg>
          </button>

          <!-- Botón Ayuda y Soporte -->
          <button
            @click="modalAyudaSoporte = true"
            class="group flex items-center gap-4 px-6 py-4 bg-gradient-to-r from-gray-100 to-gray-200 text-gray-800 rounded-2xl shadow-lg hover:shadow-xl hover:from-gray-200 hover:to-gray-300 transition-all duration-300 transform hover:scale-105 border border-gray-200"
          >
            <div class="w-12 h-12 bg-gray-300/50 rounded-xl flex items-center justify-center group-hover:bg-gray-400/50 transition-all">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <div class="flex-1 text-left">
              <h3 class="font-semibold text-lg">Ayuda y soporte</h3>
              <p class="text-gray-600 text-sm">Contacta con nuestro equipo</p>
            </div>
            <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- MODALS -->
    <!-- Editar Perfil -->
    <div v-if="modalEditarPerfil" class="fixed inset-0 flex items-center justify-center bg-black/50 backdrop-blur-sm z-50 p-4">
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-md relative overflow-hidden animate-in fade-in zoom-in duration-300">
        <div class="bg-gradient-to-r from-blue-600 to-blue-700 p-6 text-white">
          <button @click="modalEditarPerfil = false" class="absolute top-4 right-4 text-white/80 hover:text-white text-2xl transition-colors">&times;</button>
          <h3 class="text-2xl font-bold mb-2">Editar perfil</h3>
          <p class="text-blue-100">Actualiza tu información personal</p>
        </div>
        <div class="p-6">
          <form @submit.prevent="guardarPerfil" class="space-y-4">
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-700">Nombre completo</label>
              <input 
                v-model="perfil.nombre" 
                class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all" 
                type="text" 
                placeholder="Ingresa tu nombre completo"
              />
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-700">Correo electrónico</label>
              <input 
                v-model="perfil.correo" 
                class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all" 
                type="email" 
                placeholder="tu@email.com"
              />
            </div>
            <div class="flex gap-3 pt-4">
              <button 
                type="button" 
                @click="modalEditarPerfil = false"
                class="flex-1 px-6 py-3 border border-gray-300 text-gray-700 rounded-xl hover:bg-gray-50 transition-colors font-medium"
              >
                Cancelar
              </button>
              <button 
                type="submit" 
                class="flex-1 bg-gradient-to-r from-blue-600 to-blue-700 text-white px-6 py-3 rounded-xl hover:from-blue-700 hover:to-blue-800 transition-all font-medium shadow-lg"
              >
                Guardar cambios
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    
    <!-- Cambiar Contraseña -->
    <div v-if="modalCambiarContrasena" class="fixed inset-0 flex items-center justify-center bg-black/50 backdrop-blur-sm z-50 p-4">
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-md relative overflow-hidden animate-in fade-in zoom-in duration-300">
        <div class="bg-gradient-to-r from-slate-600 to-slate-700 p-6 text-white">
          <button @click="modalCambiarContrasena = false" class="absolute top-4 right-4 text-white/80 hover:text-white text-2xl transition-colors">&times;</button>
          <h3 class="text-2xl font-bold mb-2">Cambiar contraseña</h3>
          <p class="text-slate-100">Mantén tu cuenta segura</p>
        </div>
        <div class="p-6">
          <form @submit.prevent="guardarContrasena" class="space-y-4">
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-700">Contraseña actual</label>
              <input 
                v-model="contrasena.actual" 
                class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-slate-500 focus:border-transparent transition-all" 
                type="password" 
                placeholder="Contraseña actual"
              />
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-700">Nueva contraseña</label>
              <input 
                v-model="contrasena.nueva" 
                class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-slate-500 focus:border-transparent transition-all" 
                type="password" 
                placeholder="Nueva contraseña"
              />
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-700">Confirmar nueva contraseña</label>
              <input 
                v-model="contrasena.confirmar" 
                class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-slate-500 focus:border-transparent transition-all" 
                type="password" 
                placeholder="Confirmar contraseña"
              />
            </div>
            <div class="flex gap-3 pt-4">
              <button 
                type="button" 
                @click="modalCambiarContrasena = false"
                class="flex-1 px-6 py-3 border border-gray-300 text-gray-700 rounded-xl hover:bg-gray-50 transition-colors font-medium"
              >
                Cancelar
              </button>
              <button 
                type="submit" 
                class="flex-1 bg-gradient-to-r from-slate-600 to-slate-700 text-white px-6 py-3 rounded-xl hover:from-slate-700 hover:to-slate-800 transition-all font-medium shadow-lg"
              >
                Actualizar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Ayuda y Soporte -->
    <div v-if="modalAyudaSoporte" class="fixed inset-0 flex items-center justify-center bg-black/50 backdrop-blur-sm z-50 p-4">
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-md relative overflow-hidden animate-in fade-in zoom-in duration-300">
        <div class="bg-gradient-to-r from-gray-700 to-gray-800 p-6 text-white">
          <button @click="modalAyudaSoporte = false" class="absolute top-4 right-4 text-white/80 hover:text-white text-2xl transition-colors">&times;</button>
          <h3 class="text-2xl font-bold mb-2">Ayuda y soporte</h3>
          <p class="text-gray-100">Estamos aquí para ayudarte</p>
        </div>
        <div class="p-6">
          <div class="space-y-6">
            <div class="flex items-center gap-4 p-4 bg-blue-50 rounded-xl border border-blue-100">
              <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                </svg>
              </div>
              <div>
                <p class="font-semibold text-gray-800">Email</p>
                <p class="text-blue-600 font-medium">soporte@mindsecure.com</p>
              </div>
            </div>
            
            <div class="flex items-center gap-4 p-4 bg-green-50 rounded-xl border border-green-100">
              <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                </svg>
              </div>
              <div>
                <p class="font-semibold text-gray-800">Teléfono</p>
                <p class="text-green-600 font-medium">+57 123 456 7890</p>
              </div>
            </div>

            <div class="flex items-center gap-4 p-4 bg-purple-50 rounded-xl border border-purple-100">
              <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
                <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <div>
                <p class="font-semibold text-gray-800">Horario de atención</p>
                <p class="text-purple-600 font-medium">Lun - Vie: 8:00 AM - 6:00 PM</p>
              </div>
            </div>
          </div>
          
          <button 
            class="w-full mt-6 bg-gradient-to-r from-gray-700 to-gray-800 text-white px-6 py-3 rounded-xl hover:from-gray-800 hover:to-gray-900 transition-all font-medium shadow-lg" 
            @click="modalAyudaSoporte = false"
          >
            Cerrar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const modalEditarPerfil = ref(false)
const modalCambiarContrasena = ref(false)
const modalAyudaSoporte = ref(false)

const perfil = reactive({
  nombre: 'Dr. Juan Carlos Médico',
  correo: 'medico@mindsecure.com'
})

function guardarPerfil() {
  modalEditarPerfil.value = false
  // Aquí puedes agregar la lógica para guardar en tu backend
  console.log('Perfil actualizado:', perfil)
  // Mostrar notificación de éxito
}

const contrasena = reactive({
  actual: '',
  nueva: '',
  confirmar: ''
})

function guardarContrasena() {
  if (contrasena.nueva !== contrasena.confirmar) {
    alert('Las contraseñas no coinciden')
    return
  }
  if (contrasena.nueva.length < 8) {
    alert('La contraseña debe tener al menos 8 caracteres')
    return
  }
  
  modalCambiarContrasena.value = false
  // Limpiar campos
  contrasena.actual = ''
  contrasena.nueva = ''
  contrasena.confirmar = ''
  
  // Aquí puedes agregar la lógica para actualizar en tu backend
  console.log('Contraseña actualizada')
  // Mostrar notificación de éxito
}
</script>

<style scoped>
.animate-in {
  animation: slideIn 0.3s ease-out;
}

.fade-in {
  animation: fadeIn 0.3s ease-out;
}

.zoom-in {
  animation: zoomIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes zoomIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
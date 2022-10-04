import 'bootstrap/dist/css/bootstrap.min.css'
import 'assets/main.css'

<template>
  <HeaderComponent></HeaderComponent>
  <component :is = "currentView" />
  <FooterComponent></FooterComponent>
</template>

<script>
import Home from './pages/home.vue';
import NotFound from './pages/NotFound.vue';
import HeaderComponent from './components/header-component.vue';
import FooterComponent from './components/footer-component.vue';
import registroPacienteVue from './pages/registro-paciente.vue';
import consultaPacienteVue from './pages/consulta-paciente.vue';
import inicioSesionVue from './pages/inicio-sesion.vue';


const routes = {
  '/' : Home,
  '/registrar-paciente' : registroPacienteVue,
  '/consultar-paciente' : consultaPacienteVue,
  '/iniciar-sesion' : inicioSesionVue,
}

export default {
  name: 'App',
  data() {
    return {
      currentPath : window.location.hash
    }
  },
  computed: {
    currentView(){
      return routes[
        this.currentPath.slice(1) || '/'
      ] || NotFound
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
      this.currentPath = window.location.hash
    })
  },
  components: {HeaderComponent , FooterComponent}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

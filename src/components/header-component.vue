<template>
    <div id="contenedor">
        <div id="logo">
            <img v-bind:src="require('./../assets/Logo SHC.jpeg')" alt="logo">
        </div>
        <div id="menu">
            <nav>
                <li>
                    <a href="">Registrar</a>
                    <nav id="submenu">
                        <li>
                            <a href="#/registrar-paciente">Paciente</a>
                        </li>
                        <li>
                            <a href="">Médico</a>
                        </li>
                        <li>
                            <a href="">Enfermero</a>
                        </li>
                        <li>
                            <a href="">Familiar</a>
                        </li>
                    </nav>
            </li>
            <li>
                <a href="">Asignar</a>
            </li>
            <li>
                <a href="#/consultar-paciente">Consultar</a>
            </li>
            <li>
                <a href="#/iniciar-sesion">Iniciar Sesión</a>
            </li>
        </nav>
    </div>
    </div>
</template>
<script>
    export default {
      name: 'header-component',
      props: {
        msg: String
      }
    }
</script>
<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300&display=swap');
    #contenedor{
        display: flex;
        flex-direction: column;
    }
    #menu{
        width: 100%;
        height: auto;
        background-color: rgba(0, 126, 245, 0.678);
    }
    nav{
        list-style: none;
        display: flex;
        justify-content: space-evenly;
    }
    nav > li{
        float: left;
    }
    nav > li > a{
        text-decoration: none;
        padding: 10px 12px;
        color: rgb(255, 255, 255);
        font-size: 25px;
        font-weight: 700;
        font-family: 'Quicksand', sans-serif;
    }
    #submenu{
        display: none;
        position: absolute;
        background-color: rgba(0, 126, 245, 0.678);
        border: 7px dotted #007EF5;
        border-radius: 40px 40px 40px 40px;
    }
    nav li:hover > #submenu{
        display: flex;
        flex-direction: column;
        padding-top: 15px;
    }
    #submenu > li{
        padding: 7px 0 0 0;
    }
</style>
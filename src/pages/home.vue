<template>
    <div id="container-home" class="container">
        <img v-bind:src="require('./../assets/foto-medico.jpg')" alt="medico-en-casa" class="imagen">
        <div class="eslogan">
            <span>Al cuidado de tu salud sin salir de casa</span>
        </div>
    </div>
</template>
<script>
    export default {
    name: "home-page",
    props: {
        msg: String
    },
    components: {}
}
</script>
<style scoped>
.container{
    height: 750px;
    width: 100%;
}
.imagen{
    object-fit: cover;
    width: 100%;
    height: 750px;
}
.eslogan{
    font-family: 'Quicksand', sans-serif;
    position: relative;
    top: -250px;
    left: 30%;
    background-color: rgba(27, 158, 233, 0.63);
    color: #fff;
    height: auto;
    width: 500px;
    font-size: 50px;
    
}
</style>
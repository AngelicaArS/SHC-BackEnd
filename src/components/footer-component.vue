<template>
    <div id="contenedor-footer" class="footer">
      <span class="copyright">2022 © Sistema de Hospitalización en Casa</span>
    </div>

</template>
<script>
    export default {
      name: 'footer-component',
      props: {
        msg: String
      }
    }
</script>
<style scoped>
.footer{
  background-color: rgba(0, 126, 245, 0.678);
  height: 100px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.copyright{
  font-family: 'Quicksand', sans-serif;
  font-size: 20px;
  font-weight: 700;
  color: #fff;
  text-align: center;
}
</style>
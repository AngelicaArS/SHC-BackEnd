<template>
    <div class="vue-tempalte">
        <form>
            <h3>Registro Paciente</h3>
 
            <div class="form-group">
                <label>Nombre: </label>
                <input type="text" class="form-control form-control-lg"/>
            </div>
 
             <div class="form-group">
                <label>Apellido: </label>
                <input type="text" class="form-control form-control-lg"/>
            </div>

            <div class="form-group">
                <label>Correo electrónico: </label>
                <input type="email" class="form-control form-control-lg" />
            </div>
 
            <div class="form-group">
                <label>Contraseña: </label>
                <input type="password" class="form-control form-control-lg" />
            </div>

             <div class="form-group">
                <label>Teléfono: </label>
                <input type="text" class="form-control form-control-lg"/>
            </div>

             <div class="form-group">
                <label>Género: </label>
                <input type="text" class="form-control form-control-lg"/>
            </div>

             <div class="form-group">
                <label>Fecha/Nacimiento: </label>
                <input type="text" class="form-control form-control-lg"/>
            </div>

             <div class="form-group">
                <label>Ciudad de residencia: </label>
                <input type="text" class="form-control form-control-lg"/>
            </div>

            <div class="form-group">
                <label>Dirección: </label>
                <input type="text" class="form-control form-control-lg"/>
            </div>

  <h3>Personal a cargo del paciente</h3>

          <div class="form-group">
                <label>ID Médico/a a cargo: </label>
                <input type="text" class="form-control form-control-lg" />
            </div>

          <div class="form-group">
                <label>ID Enfermero/a a cargo: </label>
                <input type="text" class="form-control form-control-lg" />
            </div>
  
            <div class="form-group">
                <label>ID Cuidador/a a cargo: </label>
                <input type="text" class="form-control form-control-lg" />
            </div>
 
             <div class="btnSurrender">
            <button type="submit" class="btn btn-dark btn-lg btn-block">Registrar Paciente</button>
             </div>
 

        </form>
    </div>
</template>
<script>
    export default {
      name: 'registro-paciente',
      props: {
        msg: String
      }
    }
</script>
<style scoped>
label{
  font-weigth:bold;
}

.form-group{
  padding: 5px;
}

.btn{
padding: 5px;
}
.btnSurrender{
  padding: 10px;
}

</style>
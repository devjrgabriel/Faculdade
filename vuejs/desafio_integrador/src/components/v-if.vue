<template>
    <TheHeader v-show="mostrarheader" />
    <div v-if="verificacao_usuario === 'admin'">Ola admin</div>
    <div v-else-if="verificacao_usuario === 'marketing'">Ola marketing</div>
    <div v-else>Ola Usuario</div>
</template>


<script>

export default {
    data() {
        return {
            mostrarheader: true,
            verificacao_usuario: 'admin'
        }
    }

}


</script>

<style>
.header {
    background-color: black;
    color: white;
    margin: 0;
    padding: 0;
}
</style>
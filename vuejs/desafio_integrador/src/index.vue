<template>
  <TheHeader v-show="mostrarheader" />
  <div v-if="verificacao_usuario === 'admin'">Ola admin</div>
  <div v-else-if="verificacao_usuario === 'marketing'">Ola marketing</div>
  <div v-else>Ola Usuario</div>
</template>

<script>
import TheHeader from './components/TheHeader.vue';

export default {
  name: 'App',
  components: {
  
    TheHeader
  },
  data() {
    return {
      mostrarheader: true,
      verificacao_usuario: 'admin'
    }
  }
}
</script>

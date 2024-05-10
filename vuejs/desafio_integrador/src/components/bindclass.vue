<template>
    <h1 :class="{ 'title': true, 'titlehome': ishome }">Aqui é utilizando objeto</h1>
    <h1>Aqui é utilizando classe e objeto</h1>



</template>
<script>
export default {
    name: 'App',
    data() {
        return {
            ishome: true,
        }
    }

}
</script>
<style>
.title {
    color: red;
}

.titlehome {
    font-size: 40px;
}
</style>
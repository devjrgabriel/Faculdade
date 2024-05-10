<!-- <template>
    <vfor />
</template>
<script>
import vfor from "./components/v-for.vue";

export default {
    name: 'App',
    components: {
        vfor
    }
}

</script>
 -->

<template>
    <div>
        <h1 :class="{ 'title': true }">Aqui é estilização com bind</h1>
        <h1 :class="{ 'title': true, 'titlehome': ishome }">Aqui é estilização com bind</h1>
        <div v-for="(obj, index) in todos" v-bind:key="obj.id" class="v-for">
            <img :src="obj.imglink" alt="" v-if="obj.imglink" srcset="">
            {{ index }} - {{ obj.title }}
        </div>




    </div>
</template>


<script>

export default {
    data() {
        return {
            todos: [
                {
                    "userId": 1,
                    "id": 1,
                    "title": "delectus aut autem",
                    "completed": false,
                    "imglink": 'https://via.placeholder.com/50'
                },
                {
                    "userId": 1,
                    "id": 2,
                    "title": "quis ut nam facilis et officia qui",
                    "completed": false,
                    "imglink": 'https://via.placeholder.com/50'

                },
                {
                    "userId": 1,
                    "imglink": 'https://via.placeholder.com/50',
                    "id": 3,
                    "title": "fugiat veniam minus",
                    "completed": false
                },
                {
                    "userId": 1,
                    "id": 4,
                    "title": "et porro tempora",
                    "completed": true
                },
                {
                    "userId": 1,
                    "id": 5,
                    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
                    "completed": false
                }
            ],
            ishome: true

        }
    }

}


</script>

<style>
.title {
    background-color: red
}

.titlehome {
    color: white;
    background-color: green;
}

.v-for {
    background-color: black;
    color: white;
    margin: 0;
    padding: 0;
    text-align: center;
    padding: 1rem;
}
</style>
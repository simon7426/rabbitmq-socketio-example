<script setup>
import axios from 'axios'

const user_id = Math.floor(Math.random() * 100);

async function clickButton(){
    const url = `http://hello.world/publish/${user_id}`
    await axios.get(url)
}

</script>


<template>
  <div class="flex flex-col items-center justify-center">
    <div class="">
        <h1>Hello {{ user_id }}</h1>
    </div>
    <div class="">
        <button @click="clickButton"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold w-48 py-2 px-4 rounded"
        >
          Click Me!
        </button>
    </div>
  </div>
</template>

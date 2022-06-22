<script setup>
import { ref, inject } from "vue";
import GridBoxTableView from './GridBoxTableView.vue'

const socket = inject("socket");
const winners = ref([]);

socket.on("connect", () => {
  socket.emit("join");
});

socket.on("status", (val) => {
  if (winners.value.length >= 5) {
    winners.value.pop();
  }
  if (val.winner != -1) {
    winners.value.unshift({"winner": val.winner, "key": Math.floor(Math.random() * 10000000)});
  }
//   console.log(val.winner);
});
</script>

<template>
  <GridBoxTableView :winners="winners" />
</template>

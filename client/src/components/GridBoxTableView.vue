<script>
export default {
  props: ["winners"],
};
</script>

<template>
  <div class="flex items-center justify-center text-center">
    <table class="table-auto">
      <thead>
        <tr>
          <th>Past Winners</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="winner in winners" :key="winner.key">
          <tr>
            <td>{{ winner.winner }}</td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

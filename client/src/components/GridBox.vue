<script>
import GridBoxButton from './GridBoxButton.vue';
import GridBoxTable from './GridBoxTable.vue';
export default {
    components: { GridBoxButton, GridBoxTable }
}
</script>

<template>
    <div class="grid grid-cols-3 gap-4">
        <div class="col-span-2">
            <GridBoxTable />
        </div>
        <div>
            <GridBoxButton />
        </div>
    </div>
</template>
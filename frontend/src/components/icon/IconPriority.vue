<template>
    <el-icon v-if="props.priority == 'High'" style="transform: rotate(270deg);">
        <DArrowRight :class="props.color" />
    </el-icon>
    <el-icon v-if="props.priority == 'Medium'">
        <DCaret :class="props.color" />
    </el-icon>
    <el-icon v-if="props.priority == 'Low'" style="transform: rotate(90deg);">
        <DArrowRight :class="props.color" />
    </el-icon>
</template>

<script setup>
const props = defineProps(['color', 'priority'])

</script>

<style lang="scss" scoped></style>
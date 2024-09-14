<template>
    <div class="flex  item-center justify-start bg-red-500 p-3">
        <div class="flex flex-1">
            <div class="flex items-center space-x-3">
                <div @click="toggleMenu" class="flex flex-col items-center space-y-1 cursor-pointer">
                        <div class="w-[25px] h-[2px] bg-white"></div>
                        <div class="w-[25px] h-[2px] bg-white"></div>
                        <div class="w-[25px] h-[2px] bg-white"></div>
                </div>
                <div>
                    <h3 class="text-base font-bold text-white">MySatnusa Platform</h3>
                    <h3 class="text-xs text-white">Project Manajement Tools</h3>
                </div>
            </div>
        </div>
        <div class="flex space-x-3">
            <div class="flex items-center justify-center">
                <el-icon>
                    <Bell color="white" />
                </el-icon>
            </div>
            <div class="">
                <h3 class="text-base font-bold text-white">Hari Nugraha</h3>
                <h3 class="text-xs text-white">Product Design</h3>
            </div>
            <div class="flex items-center justify-center">
                <el-icon>
                    <ArrowDownBold color="white" />
                </el-icon>
            </div>
        </div>
    </div>
    <!-- <SIdeMenu :menuVisible="menuVisible" :activeItem="activeItem" :toggleMenu="toggleMenu" /> -->

</template>

<script lang="ts" setup>
// import { ref } from 'vue';
const {toggleMenu} = defineProps(['toggleMenu'])

</script>

<style lang="scss" scoped></style>
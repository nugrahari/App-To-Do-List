<template>
  <div class="common-layout">
    <el-container>
      <el-header >
        <Headers :toggleMenu="toggleMenu"/>
      </el-header>
      <el-container>
        <!-- <el-aside> -->
          <SIdeMenu :menuVisible="menuVisible" :activeItem="activeItem" :toggleMenu="toggleMenu" />
           <!-- <div class="absolute top-[60px] left-0 bottom-0 w-[200px] bg-blue-300 z-50 transition-all duration-300" :class="menuVisible?'left-0':'-left-[500px]'" >

           </div> -->
        <!-- </el-aside> -->
        <el-main>
          <RouterView />
        </el-main>
      </el-container>
    </el-container>
  </div>




</template>

<script setup>
import Headers from "../Headers.vue"

import { ref } from 'vue';
const menuVisible = ref(false)
const activeItem = ref('1')

const toggleMenu = () => {
  menuVisible.value = !menuVisible.value
}
import SIdeMenu from '../SIdeMenu.vue';
</script>

<style lang="scss" scoped>
.el-header {
 padding : 0 !important
}
</style>

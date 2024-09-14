<template>
    <div class="absolute top-[64px] left-0 bottom-0 w-[300px] bg-red-100 z-50 transition-all duration-300"
        :class="menuVisible ? 'left-0' : '-left-[550px]'">

        <li v-for="(val, i) in menu " :key="i" @click="onClickMenu(val.link)" class="pt-5 pl-10 list-none cursor-pointer" >
            {{ val.nama }}
        </li>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const { menuVisible, activeItem, toggleMenu } = defineProps(['menuVisible', 'activeItem', 'toggleMenu'])

const menu = ref([
    {
        "nama": "Dashboard",
        "link": "/",
        "icon": "dashboard"
    },
    {
        "nama": "Projects",
        "link": "/projects",
        "icon": "projects"
    }
])

const router = useRouter()

const onClickMenu = (params) => {
    router.push(params)
    toggleMenu()
}
</script>

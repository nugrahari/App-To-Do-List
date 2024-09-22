<template>
    <main class="min-h-screen flex flex-col space-y-5">
        <section class="mx-4 flex flex-row justify-between">
            <div class="font-bold text-xl">
                <h1>Project Management : {{ sprint.data?.project.name }} - {{ sprint.data?.title }}</h1>
            </div>
            <div class="w-[100px] flex flex-row justify-between text-gray-400">
                <p>
                    < </p>
                        <p>1/3</p>
                        <p>></p>
            </div>
        </section>
        <section class="mx-4  flex flex-row  justify-between">
            <div class="flex flex-row  justify-start">
                <div class="mr-2">
                    <el-input v-model="filterisation.search" style="height: 50px; width: 240px" placeholder="Search">
                        <template #prefix>
                            <el-icon class="el-input__icon">
                                <search />
                            </el-icon>
                        </template>
                    </el-input>
                </div>
                <div class="mx-2">
                    <el-button style="height: 50px;" :icon="Files">Filter</el-button>
                </div>
                <div class="mx-2">
                    <FormTask :reFetchTask="getTasks" :sprintId="sprintId" />
                </div>
            </div>
            <div class="flex flex-row">
                <div class="m-1 p-2">
                    <el-text class="mx-1">
                        Priority :
                    </el-text>
                </div>
                <div class="flex flex-row items-center m-1 p-2  justify-between" v-for="(val, i) in statusProority"
                    :key="i">
                    <IconPriority :color="getColor(val)" :priority="val" />
                    <div class="ml-3">
                        <el-text class="p-2 mx-1" :type="getColorPriority(val)">
                            {{ val }}
                        </el-text>
                    </div>
                </div>
            </div>
        </section>
        <section class="flex-1 flex space-x-2 mx-4">
            <div class="bg-slate-100 min-w-[300px] flex flex-col" v-for="(val, i) in list_tasks" :key="i">
                <div class="p-2 py-3 bg-white">
                    <div class="flex justify-between items-center p-2">
                        <h1 class="font-bold text-slate-800 mb-2">{{ val.name.toUpperCase() }}</h1>
                        <div class="w-[30px] aspect-square flex justify-center items-center bg-pink-200 text-slate-700">
                            {{ val?.list?.length }}
                        </div>
                    </div>
                    <div class=" w-full h-[3px]" :class="getBgColor(val.name.toUpperCase())"></div>
                </div>
                <div class="flex flex-col">
                    <div class="bg-white p-2 h-[100px] border rounded flex flex-col space-y-2"
                        v-for="(list, ii) in val.list" :key="ii">
                        <div class="flex justify-between items-center">
                            <div class=" w-[50px] h-2 rounded-xl" :class="getBgColor(val.name)"></div>
                            <el-icon color="#555" class="cursor-pointer hover:opacity-80"
                                @click="openDialogTaskDetail(list)">
                                <Edit />
                            </el-icon>
                        </div>
                        <h1><span class="font-bold">{{ list.title }}</span> - {{ list.description }}</h1>
                        <div class="flex">
                            <div class="flex items-center space-x-2">
                                <span
                                    class="w-[20px] aspect-square text-xs bg-slate-300 text-gray-400 rounded-full flex justify-center items-center font-bold">{{
                                        getSingkatanPriority(list.priority) }}</span>
                                <IconPriority :color="getColor(val.name)" :priority="list.priority" />
                                <el-text class="mx-1" :type="getColorPriority(list.priority)">{{ list.priority
                                    }}</el-text>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <FormUpdateTask :reFetchTask="getTasks" :sprintId="sprintId" v-model:task="selectedTasks"
                v-model:dialogFormVisible="dialogFormVisible" :closeDialogTaskDetail="closeDialogTaskDetail" />
        </section>
    </main>
</template>

<script setup>
import * as API from '../../api/app.api'
import { reactive, ref } from 'vue';
import IconPriority from '../../components/icon/IconPriority.vue';
import FormTask from '../../components/modal/FormTask.vue';
import FormUpdateTask from '../../components/modal/FormUpdateTask.vue';
import { getBgColor, getColor, getColorPriority, getSingkatanPriority } from '../../helper/utils';
import { Files } from '@element-plus/icons-vue'

import { useStore } from 'vuex';

const store = useStore();
const statusCategory = ref(['To Do', 'In Progress', 'Script Testing', 'Done', 'Backlog'])
const statusProority = ref(['High', 'Medium', 'Low'])

const tasks = ref([])
const selectedTasks = ref({})
const sprint = ref({})

const list_tasks = ref([])

const filterisation = reactive({
    search: "",
    filter: "",
})


const priorityOrder = {
    'High': 1,
    'Medium': 2,
    'Low': 3
}

const getTasks = async (sprint_id) => {
    try {
        const data_sprint = await API.getSprintById(sprint_id)
        sprint.value = data_sprint
        const { data } = await API.getTasks(sprint_id)
        if (data) {
            list_tasks.value = []
            tasks.value = data
            statusCategory.value.map((status) => {
                let category = {
                    name: status,
                    list: []
                }
                data.map(task => {
                    if (status == task.status) {
                        category.list.push(task)
                    }
                })
                category.list.sort((a, b) => {
                    return priorityOrder[a.priority] - priorityOrder[b.priority]
                })
                list_tasks.value.push(category)
            })
        }
    } catch (error) {
        console.log(error)
    }
}

const dialogFormVisible = ref(false)

const openDialogTaskDetail = (item) => {
    selectedTasks.value = item
    dialogFormVisible.value = true
}

const closeDialogTaskDetail = () => {
    selectedTasks.value = {}
    dialogFormVisible.value = false
}
// Execute
const sprintId = store.state.sprintActive;
getTasks(sprintId)
</script>

<style lang="scss" scoped></style>
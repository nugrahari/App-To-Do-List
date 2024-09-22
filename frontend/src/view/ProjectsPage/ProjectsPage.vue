<template>
    <div class="m-2">
        <el-table :data="$store.state.projectList" highlight-current-row style="width: 100%"
            @current-change="handleCurrentChange">
            <el-table-column type="index" width="50" />
            <el-table-column property="name" label="Name" width="300" />
            <el-table-column property="description" label="Description" width="120" />
        </el-table>
        <div style="margin-top: 20px">
            <el-button @click="clearCurrent()">Clear selection</el-button>
            <div v-if="currentRow !== null" class="selectedProject">
                <p class="m-2">Selected</p>
                <p class="ml-2">nama: {{ currentRow?.name }} , description : {{ currentRow?.description }}</p>
                <el-table :data="sprintList" highlight-current-row style="width: 100%" @row-click="handleRowClick">
                    <el-table-column type="index" width="50" />
                    <el-table-column property="title" label="Title" width="300" />
                    <el-table-column property="start_date" label="Start Date" width="120" />
                    <el-table-column property="end_date" label="End Date" width="120" />
                </el-table>
            </div>
        </div>
    </div>
</template>


<script setup>
import * as API from '../../api/app.api'
import { useRouter } from 'vue-router';
import { onMounted, ref } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const router = useRouter()
const currentRow = ref(null)
const sprintList = ref([])

const getProjectSprints = async (projectIDSelected) => {
    try {
        let response = await API.getProjectSprints(projectIDSelected)
        sprintList.value = response.data
    } catch (error) {
        console.log(error)
    }
}

const handleCurrentChange = (val) => {
    currentRow.value = val
    getProjectSprints(val.id)
}


const handleRowClick = (row, column, event) => {
    router.push("sprint")
    store.commit("setSprintActive", row.id)
};

const clearCurrent = () => {
    currentRow.value = null
    sprintList.value = []
}
onMounted(() => {
    store.dispatch('fetchProjectList');
});

</script>

<style lang="scss" scoped></style>

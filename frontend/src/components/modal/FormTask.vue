<template>

    <el-button style="height: 50px; background-color: #C8102E; color: white;" :icon="Edit"
        @click="dialogFormVisible = true">
        Add Activity Task
    </el-button>

    <el-dialog v-model="dialogFormVisible" title="Add Activity Task" width="750">
        <el-form :model="form">
            <div class="my-2 flex flex-col">
                <p class="my-2">Title</p>
                <el-input v-model="form.title" autocomplete="off" />
            </div>
            <div class="my-2 flex flex-col">
                <p class="my-2">Description</p>
                <quill-editor theme="snow" ref="quillEditorX" v-model="form.description" @text-change="onEditorChange" style="height: 100px;"/>
            </div>
            <div class="my-2 flex flex-col">
                <p class="my-2">Priority</p>
                <el-select v-model="form.priority" placeholder="Please select Priority">
                    <el-option label='Low' value='Low' />
                    <el-option label='Medium' value='Medium' />
                    <el-option label='High' value='High' />
                </el-select>
            </div>
        </el-form>
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogFormVisible = false">Cancel</el-button>
                <el-button type="primary" @click="postTask">
                    Confirm
                </el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script setup>
// Definisikan props tanpa TypeScript
const props = defineProps(['reFetchTask', 'sprintId'])
import { Edit } from '@element-plus/icons-vue'

import { reactive, ref } from 'vue'
import * as API from "../../api/app.api"

// Kontrol visibilitas dialog
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'

// Data form
const form = reactive({
    "sprint": props.sprintId,
    "title": "",
    "description": "",
    "status": 'To Do',
    "priority": ""
})
const quillEditorX = ref(null)
const onEditorChange = (delta, oldDelta, source) => {
    if (quillEditorX.value) {
        const editor = quillEditorX.value.getText()
        form.description = editor
    }
};

const postTask = async () => {
    try {
        const response = await API.postTask(form)
        console.log('Response:', response.data)
    } catch (error) {
        console.error('Error:', error)
    }
    dialogFormVisible.value = false
    props.reFetchTask(props.sprintId)
}
</script>

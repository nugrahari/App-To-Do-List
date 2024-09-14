<template>

    <!-- <el-icon color="#555" class="cursor-pointer hover:opacity-80" @click="dialogFormVisible = true">
        <Edit />
    </el-icon> -->


    <el-dialog v-model="props.dialogFormVisible" title="Activity Task" width="750" :close-on-click-modal="false"
        :before-close="props.closeDialogTaskDetail" >
        <el-form :model="form">
            <div class="my-2 flex flex-col">
                <p class="my-2">Title</p>
                <el-input v-model="form.title" autocomplete="off" />
            </div>
            <div class="my-2 flex flex-col">
                <p class="my-2">Description</p>
                <!-- <el-input v-model="form.description" autocomplete="off" /> -->
                <quill-editor theme="snow" ref="quillEditorY" v-model="form.description" @text-change="onEditorChange"
                    style="height: 100px;" />
            </div>
            <div class="my-2 flex flex-col">
                <p class="my-2">Priority</p>
                <el-select v-model="form.priority" placeholder="Please select Priority">
                    <el-option label='Low' value='Low' />
                    <el-option label='Medium' value='Medium' />
                    <el-option label='High' value='High' />
                </el-select>
            </div>
            <div class="my-2 flex flex-col">
                <p class="my-2">Status</p>
                <el-select v-model="form.status" placeholder="Please select Priority">
                    <el-option label='To Do' value='To Do' />
                    <el-option label='In Progress' value='In Progress' />
                    <el-option label='Script Testing' value='Script Testing' />
                    <el-option label='Done' value='Done' />
                    <el-option label='Backlog' value='Backlog' />
                </el-select>
            </div>
        </el-form>
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="props.closeDialogTaskDetail()">Cancel</el-button>
                <el-button type="primary" @click="putTask">
                    Confirm
                </el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script setup>
const props = defineProps(['reFetchTask', 'sprintId', "task", "dialogFormVisible", "closeDialogTaskDetail"])
import { nextTick, onMounted, reactive, ref, watch, watchEffect } from 'vue'
import * as API from "../../api/app.api"

const formLabelWidth = '140px'

const form = reactive({
    "sprint": props.task.sprint,
    "title": props.task.title,
    "description": props.task.description,
    "status": props.task.status,
    "priority": props.task.priority
})

const quillEditorY = ref(null)
const onEditorChange = () => {
    if (quillEditorY.value) {
        const editor = quillEditorY.value.getText()
        form.description = editor
    }
};

const putTask = async () => {
    try {
        const response = await API.putTask(props.task.id, form)
        console.log('Response:', response.data)
    } catch (error) {
        console.error('Error:', error)
    }
    props.reFetchTask(props.sprintId)
    props.closeDialogTaskDetail()
}

// watchEffect(() => {
//     if (quillEditorY.value ) {
//         quillEditorY.value.setText(props.task.description);
//         if(quillEditorY.value.getText()==props.task.description){
//             console.log("sama")
//         }else{
//             console.log("tida")
//         }
//     }
// });


watch(
    () => props.dialogFormVisible,
    (newValue) => {
        if (newValue) {
            form.sprint = props.task.sprint
            form.title = props.task.title
            form.description = props.task.description
            form.status = props.task.status
            form.priority = props.task.priority
            if (quillEditorY.value ) {
                quillEditorY.value.setText(props.task.description);
            }
            // quillEditorY.value.setText(props.task.description);
        }
        // console.log(newValue)
    }
)

</script>

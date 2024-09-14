import { authAxios } from "../helper/axios.config";

export function getProject() {
    return authAxios.get("/v1/app-projects/api/projects/");
}

export function getSprintById(sprint_id) {
    return authAxios.get(`/v1/app-projects/api/sprints/${sprint_id}`);
}

export function getTasks(sprint_id) {
    return authAxios.get(`/v1/app-projects/api/sprints/${sprint_id}/tasks/`);
}

export function postTask(form) {
    return authAxios.post(`/v1/app-tasks/api/tasks/`, form);
}

export function putTask(taskId, form) {
    return authAxios.put(`/v1/app-tasks/api/tasks/${taskId}/`, form);
}

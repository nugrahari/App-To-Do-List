import { createStore } from "vuex";
import * as API from '../api/app.api'

export const store = createStore({
  modules: {},
  state: {
    projectList: [],
    sprintActive: "6b8988c9-82a9-4d21-b3b4-2944e81d736c"
  },
  mutations: {
    setProjectList(state, projects) {
      state.projectList = projects;
    },
    setSprintActive(state, newSprintId) {
      state.sprintActive = newSprintId
    }
  },
  actions: {
    async fetchProjectList({ commit }) {
      try {
        const response = await API.getProject()
        commit("setProjectList", response.data)

      } catch (error) {
        console.error("Error fetching project list:", error);
      }
    }
  }
});

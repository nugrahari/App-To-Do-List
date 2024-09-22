import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: () => import("../components/layout/DashboardLayout.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () => import("../view/HomePage/HomePage.vue"),
      },
      {
        path: "/projects",
        name: "Project",
        component: () => import("../view/ProjectsPage/ProjectsPage.vue"),
      },
      {
        path: "/sprint",
        name: "Sprint",
        component: () => import("../view/ProjectsPage/SprintPage.vue"),
      },
      {
        path: "/about",
        name: "About",
        component: () => import("../view/AboutPage/AboutPage.vue"),
      },
    ],
  },
  {
    path: "/:pathMatch(.*)",
    component: () => import("../components/layout/PageNotFound.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

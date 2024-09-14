from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SprintViewSet, SprintListByProjectView, TaskListBySprintView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'sprints', SprintViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<str:project_id>/sprints/', SprintListByProjectView.as_view(), name='sprint-list-by-project'),
    path('sprints/<str:sprint_id>/tasks/', TaskListBySprintView.as_view(), name='task-list-by-sprint'),
]

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.exceptions import NotFound
from apps.tasks.api.serializers import models as task_models, TaskSerializer
from .serializers import SprintSerializer
from .. import models
from .serializers import ProjectSerializer, SprintSerializer, UserProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUserViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectUser.objects.all()
    serializer_class = UserProjectSerializer


class SprintViewSet(viewsets.ModelViewSet):
    queryset = models.Sprint.objects.all()
    serializer_class = SprintSerializer


class SprintListByProjectView(generics.ListAPIView):
    serializer_class = SprintSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        if not project_id:
            raise NotFound("Project ID not provided")

        return models.Sprint.objects.filter(project_id=project_id)


class UserListByProjectView(generics.ListAPIView):
    serializer_class = UserProjectSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        if not project_id:
            raise NotFound("Project ID not provided")

        return models.ProjectUser.objects.filter(project_id=project_id)


class TaskListBySprintView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        sprint_id = self.kwargs.get('sprint_id')
        if not sprint_id:
            raise NotFound("Sprint ID not provided")

        return task_models.Task.objects.filter(sprint_id=sprint_id)

from rest_framework import serializers
from apps.projects import models as projects_models
from .. import models


class TaskSerializer(serializers.ModelSerializer):
    sprint = serializers.PrimaryKeyRelatedField(
        queryset=projects_models.Sprint.objects.all(),
    )

    class Meta:
        model = models.Task
        fields = ['id', 'sprint', 'title', 'description', 'status', 'priority', 'created_at', 'updated_at', 'user']
        read_only_fields = ['created_at', 'updated_at']

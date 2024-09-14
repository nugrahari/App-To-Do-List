from rest_framework import serializers
from .. import models

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class SprintSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)  # Menampilkan data lengkap saat GET
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Project.objects.all(),
        write_only=True,
        source='project'
    )

    class Meta:
        model = models.Sprint
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        return models.Sprint.objects.create(**validated_data)
    
    def update(self, instance : models.Sprint, validated_data):
        project = validated_data.pop('project', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if project is not None:
            instance.project = project
        instance.save()
        return instance
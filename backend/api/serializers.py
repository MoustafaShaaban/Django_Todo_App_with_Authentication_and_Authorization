from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'created_by', 'completed']

        extra_kwargs = {
            'created_by':  { 'read_only': True }
        }
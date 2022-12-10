from rest_framework import permissions, viewsets

from django_filters.rest_framework import DjangoFilterBackend

from todos.models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwnerOrReadOnly



class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
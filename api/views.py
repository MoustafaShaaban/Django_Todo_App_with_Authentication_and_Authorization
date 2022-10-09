from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend

from tasks.models import Todo, CustomUser
from api.serializers import TodoSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'todos': reverse('todo-list', request=request, format=format),
    })


class UserViewSet(viewsets.ModelViewSet, permissions.BasePermission):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class TodoViewSet(viewsets.ModelViewSet, permissions.BasePermission):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_by', 'completed']

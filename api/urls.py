from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'todos', views.TodoViewSet,basename="todo")
router.register(r'users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

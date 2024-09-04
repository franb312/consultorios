from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TurnoViewSet, especialidades_list, RegisterView, LoginView, LogoutView

router = DefaultRouter()
router.register(r'turnos', TurnoViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('especialidades/', especialidades_list, name='especialidades-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
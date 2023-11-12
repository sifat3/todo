from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('completed/', views.completed, name='completed'),
    path('due/', views.due, name='due'),
    path('change/<int:pk>', views.change_status, name='change')
]

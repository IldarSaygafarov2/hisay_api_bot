from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.get_users_chat_id),
    path('users/create/', views.UserCreate.as_view(), name='account-create'),
]

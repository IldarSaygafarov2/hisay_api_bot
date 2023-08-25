from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.get_users_chat_id),
    path('users/create/', views.UserCreate.as_view(), name='account-create'),
    path("services/", views.ServiceListAPIView.as_view(), name="services"),
    path("services/<str:name>/", views.get_service_id_by_name, name="service_id"),
    path("service-profile/create", views.ServiceCreate.as_view(), name="create-service-profile")
]

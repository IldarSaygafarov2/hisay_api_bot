from django.urls import path

from . import views

urlpatterns = [
    path('users/create/', views.SimpleUserProfileCreate.as_view(), name='account-create'),
    path('users/<str:chat_id>/', views.get_simple_user, name='simple-user'),
    path("simple-users-profiles/ids/", views.get_simple_users_chat_id, name="simple-users-profiles-ids"),
    path("users/code/generate/", views.generate_auth_code, name="generate-auth-code"),
    path("users/code/check/", views.check_verification_code, name="check-auth-code"),
    path("services/", views.ServiceListAPIView.as_view(), name="services"),
    path("services/<str:service_id>/requests/", views.get_user_requests_for_service, name="requests-services"),
    path("services/hashtags/add/", views.generate_tags_for_service, name="services-hashtags-add"),
    path("services/<str:service_id>/hashtags/", views.get_hashtags_by_service, name="hashtags-by-service"),
    path("services/create/", views.UserRequestCreate.as_view(), name="services-create"),
    path("services/<str:name>/", views.get_service_id_by_name, name="service_id"),
    path("services/get/<int:service_id>/", views.get_service_name_by_id, name="service_name"),
    path("service-profile/create/", views.ServiceCreate.as_view(), name="create-service-profile"),
    path("service-profiles/ids/", views.get_service_profile_ids, name="service-profiles-ids"),
]

from django.urls import path

from . import views

app_name = "usuarios"


urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("user-list/", views.userList, name="user-list"),
    path("user-detail/<str:pk>/", views.userDetail, name="user-detail"),
    path("user-create/", views.userCreate, name="user-create"),
    path("user-update/<str:pk>/", views.userUpdate, name="user-update"),
    path("user-delete/<str:pk>/", views.userDelete, name="user-delete"),
]

# urlpatterns = [
#     path("api/", views.UserListView.as_view()),
#     path("api/<str:email>/", views.UserListView.as_view()),
#     path("create/", CreateUserView.as_view()),
# ]

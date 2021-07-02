from django.urls import path

from emarket.users.views import UserListView, UserViewSet

urlpatterns = [
    path("", view=UserListView.as_view(), name="users"),
    path("<str:username>/", view=UserViewSet.as_view(), name="user")
]

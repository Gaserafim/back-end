from django.urls import path
from users.views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    UserUpdateView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/update/", UserUpdateView.as_view(), name="profile-update"),
]

from django.urls import path

from apps.account.api_endpoints import  auth

urlpatterns = [
    path("register/", auth.RegisterView.as_view(), name="register"),
    path("login/", auth.LoginView.as_view(), name="login"),
    # path(
    #     "google-auth/",
    #     social_auth.GoogleSocialAuthView.as_view(),
    #     name="google-socail-auth",
    # ),
    # path(
    #     "facebook-auth/",
    #     social_auth.FacebookSocialAuthView.as_view(),
    #     name="facebook-social-auth",
    # ),
]

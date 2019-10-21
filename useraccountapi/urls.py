from django.urls import path

from useraccountapi.views import LoginView, RegisterUsers, UserCreate

urlpatterns = [
    # ...

    # Some where in your existing urlpatterns list, Add this line
    path('auth/login/', LoginView.as_view(), name="auth-login"),

    # ...
    # Some where in your existing urlpatterns list, Add this line
    # path('auth/register/', RegisterUsers.as_view(), name="auth-register"),

    path('auth/register/', UserCreate.as_view(), name="auth-register"),

    # ...
]

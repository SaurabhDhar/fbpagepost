from django.urls import path
from .views import login,home,sharing
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',sharing,name='home'),
    # path('', home, name='home'),
    path("login/", login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

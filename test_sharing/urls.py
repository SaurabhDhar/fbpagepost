from django.urls import path
from .views import login,sharing,add_post
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sharing/',sharing,name='home'),
    path("login/", login, name="login"),
    path('add/post/',add_post, name='add_post')
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

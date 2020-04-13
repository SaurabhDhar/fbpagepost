from django.urls import path
from .views import login,sharing,add_post
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404


handler404 = 'test_sharing.views.handler404'

urlpatterns = [
    path('sharing/',sharing,name='home'),
    path("login/", login, name="login"),
    path('add/post/',add_post, name='add_post')
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

from django.contrib import admin
from django.urls import include, path
from auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home_page_view, name="home"),
    path("login/", auth_views.login_view),
    path("register/", auth_views.register_view),
    path('accounts/', include('allauth.urls')),
]

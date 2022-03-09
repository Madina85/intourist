from django.urls import URLPattern, path
from .views import homepage, profile

urlpatterns = [
    path('', homepage, name='homepage'),
    path('profile/', profile, name='profile'),
]
from django.urls import path
from .views import profile, signup


urlpatterns = [
    path('profile/', profile, name="profile"),
    path('signup/', signup, name="signup"),
]

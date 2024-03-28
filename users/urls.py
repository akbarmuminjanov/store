from django.urls import path
from .views import profile, signup, login, logout


urlpatterns = [
    path('profile/', profile, name="profile"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]

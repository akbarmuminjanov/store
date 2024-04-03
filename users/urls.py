from django.urls import path
from .views import cart_detail, signup, login, logout


urlpatterns = [
    path('profile/', cart_detail, name="cart_detail"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]

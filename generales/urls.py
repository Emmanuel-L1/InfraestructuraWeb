from django.urls import path

from generales.views import home, login, logout

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]


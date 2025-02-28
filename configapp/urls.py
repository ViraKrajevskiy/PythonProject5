from  django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('movies/<str:genre>/', , name='movies_by_genre'),
]



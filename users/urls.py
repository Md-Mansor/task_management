from django.urls import path
from users.views import user
urlpatterns = [
    path("dashboard/", user)
    
]

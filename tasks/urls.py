from django.urls import path
from tasks.views import home, dashboard, user_dashboard 

urlpatterns = [    
    path("",home),
    path("dashboard/",dashboard),
    path("user/", user_dashboard)
]

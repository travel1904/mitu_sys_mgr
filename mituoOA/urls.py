from django.urls import path, include

urlpatterns = [
    path('', include('myadmin.urls', namespace='myadmin')),
]

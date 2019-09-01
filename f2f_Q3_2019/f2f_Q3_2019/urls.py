from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/REST/', include('api.v1.REST.urls')),
    path('api/v1/GRAPH/', include('api.v1.GRAPH.urls')),
    path('admin/', admin.site.urls)
]

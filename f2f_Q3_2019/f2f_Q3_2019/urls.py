from django.urls import path, include

urlpatterns = [
    path('api/REST/', include('api.v1.REST.urls')),
    path('api/GRAPH/', include('api.v1.GRAPH.urls')),
]

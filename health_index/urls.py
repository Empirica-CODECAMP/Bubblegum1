from django.urls import path
from .views import health_index_view

urlpatterns = [
    path('', health_index_view, name='health_index'),
]

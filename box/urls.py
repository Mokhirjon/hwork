from django.urls import path
from .views import OurAPIView

urlpatterns = [
    path('all/', OurAPIView.as_view())
]

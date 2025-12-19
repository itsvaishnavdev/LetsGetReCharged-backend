from django.urls import path
from .views import ChargerSearchAPIView

urlpatterns = [
    path("search/", ChargerSearchAPIView.as_view()),
]

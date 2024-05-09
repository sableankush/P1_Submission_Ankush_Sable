from django.urls import path
from .views import (
    AllFacility,
    NearByFacility
)

urlpatterns = [
    path('all/', AllFacility.as_view()),
    path('nearby/', NearByFacility.as_view()),
]
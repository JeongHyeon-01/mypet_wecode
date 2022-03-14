from django.urls import path
from mypet.views import OwnerView,DogView

urlpatterns = [
    path('owner', OwnerView.as_view()),
    path('dog',DogView.as_view())
]
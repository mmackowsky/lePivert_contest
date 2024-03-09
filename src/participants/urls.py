from django.contrib import admin
from django.urls import path

from .views import ParticipantListView, RandomWinnerView

urlpatterns = [
    path('', ParticipantListView.as_view(), name='participant-list'),
    path('winner/', RandomWinnerView.as_view(), name='random-winner')
]
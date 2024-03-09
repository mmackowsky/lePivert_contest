from django.shortcuts import render
from django.views.generic import ListView, View
import random

from .models import Participant


class ParticipantListView(ListView):
    model = Participant
    context_object_name = 'participants'
    template_name = 'participants/participants_list.html'

    def get_queryset(self):
        queryset = Participant.objects.all()
        return queryset


class RandomWinnerView(ListView):
    model = Participant
    template_name = 'participants/winner.html'

    def get(self, request, *args, **kwargs):
        participants = list(Participant.objects.all())
        random.shuffle(participants)
        winner = participants[0]
        return render(request, self.template_name, {'winner': winner})

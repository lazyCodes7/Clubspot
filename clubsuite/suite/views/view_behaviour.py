from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from suite.models import Club
from suite.forms import EventCreateForm
from django.contrib import messages

from guardian.shortcuts import get_perms
from django.core.exceptions import PermissionDenied

class Behaviour(UserPassesTestMixin, LoginRequiredMixin, TemplateView):

  template_name = 'behaviour.html'

  # testing for proper permissions
  def test_func(self):
    club = get_object_or_404(Club, pk=self.kwargs['club_id'])
    if 'can_create_event' not in get_perms(self.request.user, club):
      raise PermissionDenied

    return True

  def get(self, request, club_id):
    club = get_object_or_404(Club, pk=club_id)

    return render(request, self.template_name, { 'club':club })

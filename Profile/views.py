from django.shortcuts import render
from adrf.viewsets import ViewSet
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.authtoken.admin import User

from Profile.models import Profile


# Create your views here.
class ProfileView(TemplateView):
    """
    This view is used for displaying profile information
    """

    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        return {'context', context}

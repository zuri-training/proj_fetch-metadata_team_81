from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render

# Create your views here.

class Pdf(View):

    def get(self, request) :
        proj_fetch_metadata_team_81 = proj_fetch_metadata_team_81.objects.all()
        params = {
            'proj_fetch_metadata_team_81' : proj_fetch_metadata_team_81
        }

        return Render.render('pdf.html', params)
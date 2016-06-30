from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ResultsPageView(TemplateView):
    template_name = 'results.html'

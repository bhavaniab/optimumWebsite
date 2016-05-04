from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView

from django.template.loader import get_template


#Commenting the two lines for reference in the future
#def index(request):
#    return HttpResponse("Welcome to optimum website")

class IndexView(TemplateView):
    template_name = 'index.html'



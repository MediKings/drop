from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    template_name = 'home/index.html'
    return render(request, template_name)

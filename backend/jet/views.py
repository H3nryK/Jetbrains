from django.shortcuts import render
from .models import *

def main_view(request):
    return render(request, 'main.html')
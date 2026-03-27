from django.shortcuts import render

from .models import Recommendation

def form_recommendation(request):
    return render(request, 'recommendations/form.html')

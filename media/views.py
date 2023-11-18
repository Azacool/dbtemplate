from django.shortcuts import render
from .models import Portfolio

def main(request):
    portfolio = Portfolio.objects.all()
    return render(request=request,template_name='index.html',context={'portfolio':portfolio})
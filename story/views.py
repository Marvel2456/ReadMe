from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    context={}
    return render(request, 'story/index.html', context)
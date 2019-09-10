from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# The home view
def home(request):
    return HttpResponse('Hello There')

def about(request):
    return render(request, 'about.html')
from django.shortcuts import render
from .models import Comic
# Create your views here.

# The home view
def home(request):
    return render(request, 'home.html')
# about view
def about(request):
    return render(request, 'about.html')
# comics index
def comics_index(request):
    comics = Comics.objects.all()
    return render(request, 'comics/index.html', { 'comics': comics })

    




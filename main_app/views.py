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
    comics = Comic.objects.all()
    return render(request, 'comics/index.html', { 'comics': comics })
# comic detail
def comics_detail(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    return render(request, 'comics/detail.hmtl', {'comic': comic})


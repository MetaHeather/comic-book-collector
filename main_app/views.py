from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#models
from .models import Comic
from .models import Purchase
#forms
from .forms import PurchaseForm

# Create your views here.

class ComicCreate(CreateView):
    model = Comic
    fields = '__all__'


class ComicUpdate(UpdateView):
  model = Comic
  fields = '__all__'


class ComicDelete(DeleteView):
  model = Comic
  success_url = '/comics/'


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
    purchase_form = PurchaseForm()
    return render(request, 'comics/detail.html', {
        'comic': comic,
        'purchase_form': purchase_form
        })
#add a purchase to a comic
def add_purchase(request, comic_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.comic_id = comic_id
        new_purchase.save()
    return redirect('detail', comic_id=comic_id)

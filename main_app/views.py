from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
#models
from .models import Comic, Shop, Photo
#forms
from .forms import PurchaseForm

S3_BASE_URL = 's3.us-east-2.amazonaws.com'
BUCKET = 'comic-collector-hne'


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
      # Get the toys the cat doesn't have
    shops_comic_doesnt_have = Shop.objects.exclude(id__in = comic.shops.all().values_list('id'))
    purchase_form = PurchaseForm()
    return render(request, 'comics/detail.html', {
        'comic': comic,
        'purchase_form': purchase_form,
        'shops': shops_comic_doesnt_have
        })
#add a purchase to a comic
def add_purchase(request, comic_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.comic_id = comic_id
        new_purchase.save()
    return redirect('detail', comic_id=comic_id)

def assoc_shop(request, comic_id, shop_id):
  Comic.objects.get(id=comic_id).shops.add(shop_id)
  return redirect('detail', comic_id=comic_id)

def unassoc_shop(request, comic_id, shop_id):
  Comic.objects.get(id=comic_id).shops.remove(shop_id)
  return redirect('detail', comic_id=comic_id)

class ShopList(ListView):
  model = Shop

class ShopDetail(DetailView):
  model = Shop

class ShopCreate(CreateView):
  model = Shop
  fields = '__all__'

class ShopUpdate(UpdateView):
  model = Shop
  fields = ['name', 'city']

class ShopDelete(DeleteView):
  model = Shop
  success_url = '/shops/'

def add_photo(request, comic_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, comic_id=comic_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', comic_id=comic_id)
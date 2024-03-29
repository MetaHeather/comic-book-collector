from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

TIMEOFDAY =(
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shops_detail', kwargs={'pk': self.id})

class Comic(models.Model):
    title = models.CharField(max_length=100)
    issue = models.IntegerField()
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    publishdate = models.DateField('publish date')
    shops = models.ManyToManyField(Shop)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})


class Purchase(models.Model):
    purchasedate = models.DateField('purchase date')
    purchasetime = models.CharField(
        max_length=1,
        choices=TIMEOFDAY,
        default=TIMEOFDAY[0][0]
        )
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_purchasetime_display()} of {self.purchasedate}"
    class Meta:
        ordering = ['-purchasedate']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    def __str__(self):
        return f"Photo for comic_id: {self.comic_id} @{self.url}"
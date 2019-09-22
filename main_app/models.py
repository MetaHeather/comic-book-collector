from django.db import models
from django.urls import reverse
# Create your models here.

TIMEOFDAY =(
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Comic(models.Model):
    title = models.CharField(max_length=100)
    issue = models.IntegerField()
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    publishdate = models.DateField('publish date')
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
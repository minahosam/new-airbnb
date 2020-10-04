from django.db import models
from django.utils import timezone
from datetime import date
from django.urls import reverse
# Create your models here.
smoking_avability=[ ( 'smoke' , 'smoke' ) , ( 'not smoke' , 'not smoke' ) ]
single_double=[('single','single'),('double','double')]
class airbnb(models.Model):
    title=models.CharField(max_length=20)
    adress=models.CharField(max_length=30)
    description=models.TextField(max_length=200)
    owner_mail=models.EmailField()
    house_photos=models.ImageField(upload_to='post/')
    house_state=models.BooleanField(default=True)
    arrival_date=models.DateField(default=date.today)
    departure_date=models.DateField(default=date.today)
    duration=models.DurationField()
    SMOKING_CHOICES=models.CharField(max_length=20,choices=smoking_avability)
    ROOM_STATUES=models.CharField(max_length=20,choices=single_double)
    room_price=models.FloatField(max_length=55)
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    class Meta:
        ordering=('-title',)
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
    def get_absolute_url(self):
        return reverse("airbnb_post:edit_post", kwargs={"post_id": self.id})
    
from django.contrib import admin
from .models import airbnb

# Register your models here.
class airbnbAdmin(admin.ModelAdmin):
    list_display=['title','house_state','created_at']
    list_filter=['house_state','SMOKING_CHOICES','ROOM_STATUES']
admin.site.register(airbnb,airbnbAdmin)
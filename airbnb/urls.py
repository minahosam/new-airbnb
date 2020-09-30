from django.contrib import admin
from django.urls import path
from .views import all_posts, single_post
from django.conf import settings
from django.conf.urls.static import static
app_name='airbnb'

urlpatterns = [
    path('', all_posts),
    path('<post_id>', single_post,name='airbnb_detail')
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
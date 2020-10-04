from django.contrib import admin
from django.urls import path
from .views import all_posts, single_post , new_post , post_edit
from django.conf import settings
from django.conf.urls.static import static
from airbnb.views import post_delete
app_name='airbnb'

urlpatterns = [
    path('', all_posts),
    path('/new', new_post, name='new_post'),
    path('<post_id>/edit', post_edit, name='edit_post'),
    path('<post_id>/delete', post_delete, name='delete_post'),
    path('<post_id>', single_post,name='airbnb_detail')
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
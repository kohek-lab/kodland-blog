from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/new/', views.CreatePostView.as_view(), name='new-post'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
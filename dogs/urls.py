from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from dogs.views import dogs_list, dog_info
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', dogs_list, name='dog_list'),
    path('dogs/<int:pk>/', dog_info, name='dog_info')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

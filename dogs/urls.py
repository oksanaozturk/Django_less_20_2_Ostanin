from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from dogs.views import home
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', home, name='dog_info'),
    #path('breed/', breed, name='breed'),
    #path('<int:pk>/dogs/', dogs_breed, name='dogs_breed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

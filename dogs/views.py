from django.shortcuts import render, get_object_or_404
from dogs.models import Dog


def dogs_list(request):
    '''Выводит на страницы трех питомцев'''
    dogs = Dog.objects.all()
    context = {
        'object_list': dogs
    }
    return render(request, 'dogs/dogs_list.html', context)


def dog_info(request, pk):
    '''Выводит на страницу питомца по pk.'''
    dog = get_object_or_404(Dog, pk=pk)
    context = {
        'object': dog
    }
    return render(request, 'dogs/dog_info.html', context)

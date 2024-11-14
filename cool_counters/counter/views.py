from django.shortcuts import render, get_object_or_404
from .models import Counter


def index(request):
    if len(Counter.objects.filter(key='counter')) == 0:
        counter = Counter(key='counter', value=0)
        counter.save()
    else:
        counter = get_object_or_404(Counter, key='counter')

    counter.value += 1
    counter.save()
    context = {'value': counter.value, 'sum': 99 * 10}
    return render(request, 'counter/index.html', context)


def andy(request):
    context = {'message': "Hello from Andy"}
    return render(request, 'counter/andy.html', context)

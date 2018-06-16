from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
#    return HttpResponse("Hellow, world")
#    return render(request, 'cat/index.html')
    context = {
        'name':'RyosukellyPi',
    }
    return render(request, 'cat/index.html', context)

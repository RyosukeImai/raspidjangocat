from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
#    return HttpResponse("Hellow, world")
#    return render(request, 'cat/index.html')
    """/トップページ"""
    context = {
        'name':'RyosukellyPi',
    }
    return render(request, 'cat/index.html', context)

def about(request):
    """/about"""
    return render(request, 'cat/about.html')

def info(request):
    """/info"""
    return render(request, 'cat/info.html')

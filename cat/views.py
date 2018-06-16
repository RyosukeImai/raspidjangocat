from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import CatCreateForm


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

def catlist(request):
    #    return HttpResponse("Hellow, world")
#    return render(request, 'cat/index.html')
    """/キャットリスト"""
    context = {
        'name':'RyosukellyCat',
    }
    return render(request, 'cat/cat_list.html', context)

def catadd(request):
#    context = {
#        'form':CatCreateForm()
#    }
#    return render(request, 'cat/cat_add.html', context)
    # 送信内容を元にフォームを作る　POSTじゃなければ空フォーム
    form = CatCreateForm(request.POST or None)

    # method=POST つまり送信ボタン押下時入力内容が問題なければ
    if request.method=='POST' and form_is_valid():
        form_save()
        return redirect('cat:catlist')

        # 通常時のページアクセスや入力内容に誤りがあった場合
        context = {
            'form':form
        }
    return render(request,'cat/cat_add.html',context)


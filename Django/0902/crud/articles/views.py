from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


#
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()
    

    # 코드가 index와 중복!
    # aritcles = Articles.obejcts.all()
    # context = {
    #     'articles' : articles,
    # }


    # return render(request, 'articles/index.html', context)
    # 코드가 중복 되기에 index를 서버에서 여기로 요청
    # redirect(요청 경로)
    return redirect('articles:index')

def detail(request, pk):
    # 글 하나를 조회 한다.
    article = Article.objects.get(pk=pk)
    # 조회 된 data를 html에 보여준다.
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }

    return render(request, 'articles/edit.html',context)

def update(request,pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 데이터를 수정해서 저장

    article= Article.objects.get(pk=pk)
    article.title = title
    article.content =content
    article.save()

    # 저장이 끝나면 디테일 페이지로 돌아가자

    context ={
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

    # return redirect('articles/detail.html', article.pk)  이렇게도 가능?

def delete(request, pk):
    # POST 요청 일 때
    if request.method == 'POST':
    # 데이터를 삭제
        article = Article.objects.get(pk=pk)
        article.delete()

    # 글 목록 페이지로 이동
        return render(request, 'articles/index.html')
    else:   # GET
        # return redirect('articles:detail', pk)
        return redirect('articles:index')
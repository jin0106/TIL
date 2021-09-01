from django.shortcuts import render
import random

# Create your views here.


def index(request):
    title = 'title'
    return render(request, 'articles/index.html', {'name':'Jin'})

def greeting(request):
    foods =['Apple', 'Banana', 'Peach']
    info = {
        'name' : 'Jin',
    }
    
    return render(request, 'articles/greeting.html', {'fs':foods, 'inf':info})

def dinner(request):
    foods = ['Chickecn', 'Hambuger', 'Sushi', 'Folk']
    pick = random.choice(foods)
    context = {
        'pick':pick
    }
    return render(request, 'articles/dinner.html',context)

def throw(request):
    return render(request, 'articles/throw.html')    

def catch(request):
    title = (request.GET.get('title'))

    context = {
        'title' : title
    }
    return render(request, 'articles/catch.html',context)

def read(request, username, article_number):
    print(username)
    print(article_number)
    
    context = {
        'user' :username,
        'article' : article_number
    }
    return render(request, 'articles/read.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    #return HttpResponse("อาริยะ นิเทศนพกุล")
    posts = Post.objects.all()
    
    pagesName = ['','/blog/seminar99708Jan', '/blog/seminar99708Dec', '/blog/seminar99709Dec',
                 '/blog/phuket', '/blog/resources_research', '/blog/checkout_payment']    
    
    pagesDict = {}
    for post in posts:
        pagesDict.update({post.id : pagesName[post.id]})   

    return render(request, 'index.html', 
        {
            'test' : posts,
            'pagesDict' : pagesDict
        })

def seminar99708Jan(request):
    return render(request, 'seminar99708Jan.html')

def seminar99708Dec(request):
    return render(request, 'seminar99708Dec.html')

def seminar99709Dec(request):
    return render(request, 'seminar99709Dec.html')

def phuket(request):
    return render(request, 'phuket.html')

def resources_research(request):
    return render(request, 'resources_research.html')

def checkout_payment(request):
    return render(request, 'checkout_payment.html')

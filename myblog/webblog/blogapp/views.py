from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    #return HttpResponse("อาริยะ นิเทศนพกุล")
    posts = Post.objects.all()

    
    pagesName = ['','/blog/seminar99708Jan', '/blog/seminar99708Dec', '/blog/seminar99709Dec',
                 '/blog/phuket', '/blog/tempPage5', '/blog/tempPage6']    
    
    pagesDict = {}
    for post in posts:
        pagesDict.update({post.id : pagesName[post.id]})
        print('post : ', post)
        print('pagesDict : ', pagesDict)
        print('pagesDict.get() : ', pagesDict.get(post.id))       
    
    testDict = {posts}

    return render(request, 'index.html', 
        {
            'test' : posts,
            'pagesDict' : pagesDict
        })

def seminar99708Jan(request):
    return render(request, 'seminar99708Jan.html',
        {
            'testData_seminar99708_Jan' : 'seminar99708_Jan'
        })

def seminar99708Dec(request):
    return render(request, 'seminar99708Dec.html',
        {
            'testData_seminar99708_Dec' : 'seminar99708_Dec'
        })

def seminar99709Dec(request):
    return render(request, 'seminar99709Dec.html',
        {
            'testData_seminar99708_Dec' : 'seminar99708_Dec'
        })

def phuket(request):
    return render(request, 'phuket.html',
        {
            'testData_phuket' : 'phuket'
        })

def tempPage5(request):
    return render(request, 'tempPage5.html',
        {
            'testData_tempPage5' : 'stempPage5'
        })

def tempPage6(request):
    return render(request, 'tempPage6.html',
        {
            'testData_tempPage6' : 'stempPage6'
        })

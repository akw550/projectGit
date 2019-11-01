# i have created this file -AK

from django.http import HttpResponse

from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello")

# def about(request):
#     return HttpResponse("About Page")


#           ---------lecture before----------

def index(request):
    # return HttpResponse("Home")
    # param = {'name' : 'Akhlaq', 'place' : 'Earth'}

    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")


# def capfirst(request):
#     return HttpResponse("capitalize first <a href=http://127.0.0.1:8000>Back</a>")

# def newlineremove(request):
#     return HttpResponse("new line remove <a href=http://127.0.0.1:8000>Back</a>")

# def spaceremove(request):
    return HttpResponse("space remove <a href=http://127.0.0.1:8000>Back</a>")
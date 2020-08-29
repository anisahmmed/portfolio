from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("THis is my portfolio website...")
    context = {
        'name' : 'Anis',
        'course' : 'Django'
    }
    return render(request, 'home.html', context)
    
def about(request):
    # return HttpResponse("THis is about page...")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("THis is my project page...")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("THis is my contact page...")
    return render(request, 'contact.html')
    
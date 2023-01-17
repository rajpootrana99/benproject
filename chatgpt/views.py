from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context = {
        'page_name' : "Upload Video"
    }
    return render(request, 'index.html', context)

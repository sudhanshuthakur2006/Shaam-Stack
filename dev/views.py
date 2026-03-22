from django.shortcuts import render

# Create your views here.
def developer(request):
    return render (request,'dev/dev_page.html')
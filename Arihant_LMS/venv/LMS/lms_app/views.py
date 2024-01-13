from django.shortcuts import redirect, render

# Create your views here.
def BASE(request):
    return render(request, 'base.html')

def INDEX(request):
    return render(request, 'main/home.html')

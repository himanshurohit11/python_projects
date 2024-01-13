from django.shortcuts import redirect,render


def BASE(request):
    return render(request, 'base.html')


def INDEX(request):
    return render(request, 'main/index.html')


def SINGLE_COURSE(request):
    return  render(request, 'main/single_course.html')


def CONTACT_US(request):
    return render(request, 'main/contact_us.html')


def ABOUT_US(request):
    return render(request, 'main/about_us.html')

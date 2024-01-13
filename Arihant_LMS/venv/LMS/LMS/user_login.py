from django.shortcuts import render, redirect


def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("DATA--->", username, email, password)
        # # check email
        # if User.objects.filter(email=email).exists():
        #    messages.warning(request,'Email are Already Exists !')
        #    return redirect('register')
        #
        # # check username
        # if User.objects.filter(username=username).exists():
        #    messages.warning(request,'Username are Already exists !')
        #    return redirect('register')
        #
        # user = User(
        #     username=username,
        #     email=email,
        # )
        # user.set_password(password)
        # user.save()
        # return redirect('login')

    return render(request, 'registration/register.html')

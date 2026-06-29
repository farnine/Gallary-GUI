from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.


def home(request):
    return render(request,"base/index.html")


def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data.get("password")
            user.set_password(password)

            user.save()

            return redirect("home")
        
    else:
        form=RegisterForm()
    
    context={"form":form}

    return render(request,"base/register.html",context)
from django.shortcuts import render,redirect,get_object_or_404
from .models import Image
from django.urls import reverse_lazy
from .forms import RegisterForm, CustomAuthenticationForm,ImageForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    image_data=Image.objects.all()

    context={"data":image_data}
    return render(request,"base/index.html",context)


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


class CustomLoginView(LoginView):
    template_name="base/login.html"
    authentication_form=CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy("home")
    
@login_required
def upload_Image(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        print(form.errors)
        print(form.is_valid())
        print(request.FILES)
        if form.is_valid():
            
            profile=form.save(commit=False)
            profile.upload_by=request.user
            profile.save()


            return redirect("home")

    else:
        form=ImageForm()

    context={'form':form}

    return render(request, "base/upload.html", context)
    


def details(request,pk):
    image= get_object_or_404(Image, id=pk)

    context={"image":image}
    return render(request,"base/image_details.html",context)

def delete_image(request,pk):
    image=get_object_or_404(Image, id=pk)

    if request.method=="POST":
        image.delete()
        return redirect("home")
    
    return render(request, "base/delete_image.html")



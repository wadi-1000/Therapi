from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import UploadNewArticle,MakeAppointment
from .models import Articles,Appointments
# Create your views here.
def landing(request):
    return render(request,'landing.html')

def home(request):
    return render (request, 'home.html')

@login_required
def uploadArticle(request):
    form=UploadNewArticle()
    current_user=request.user

    if request.method =="POST":
        form=UploadNewArticle(request.POST, request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.user=current_user
            article.save()

        return redirect('articles')

    else:
        form=UploadNewArticle()

    return render(request, 'uploadarticle.html', {"form":form})



def viewArticles(request):
    
    article= Articles.objects.all()
    context = {
       
        'article':article
      }

    return render(request,'home.html', context)

@login_required
def singleArticle(request,pk):
    article=Articles.objects.filter(id=pk)
    current_user=request.user


    return render(request, 'viewarticle.html', {"article":article})


@login_required
def makeAppointment(request):
    form=MakeAppointment()
    current_user=request.user

    if request.method =="POST":
        form=MakeAppointment(request.POST, request.FILES)
        if form.is_valid():
            appointment=form.save(commit=False)
            appointment.user=current_user
            appointment.save()

        return redirect('articles')

    else:
        form=MakeAppointment()

    return render(request, 'makeappointment.html', {"form":form})


def myAppointments(request):
    # appointment = Appointments.objects.all()
    appointments = Appointments.display_all_objects().order_by('-date')
    context = {
       
        'appointments':appointments
      }

    
    return render(request, 'myappointments.html', context)

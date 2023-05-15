from django.shortcuts import render
from .forms import Studform, Sform
from .models import Student
# Create your views here.
def show(request):
    return render(request,"home.html")
def register(request):
    title="New Student Registration"
    form = Studform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        clas = form.cleaned_data['s_class']
        addr = form.cleaned_data['s_addr']
        school = form.cleaned_data['s_school']
        mail = form.cleaned_data['s_email']
        email = Student.objects.filter(s_email=mail)
        if len(email)>0:
            return render(request,'ack.html',{"title":"Student Already exist try with another mail"})
        else:
             p = Student(s_name=name,s_class=clas,s_addr=addr,s_school=school,s_email=mail)
             p.save()
             return render(request,'ack.html',{"title":"Registered successfully"})
    
    
    context={
        "title":title,
        "form":form,
    }
    
    return render(request,'register.html', context)


def exist(request):
        title="All Registered  Students"
        queryset = Student.objects.all()
        context={
            "title":title,
            "queryset":queryset,
        }
        return render(request,'existing.html', context)

def search(request):
    title="Search Student"
    form=Sform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = Student.objects.filter(s_name=name)
        if len(queryset)==0:
                    return render(request,'ack.html',{'title':'Student Deatils not available Please enter Data'})
        context={
        'title':title,
        'queryset':queryset,
        }
        return render(request,'existing.html',context)
    context={
        'title':title,
        'form':form,
    }
    return render(request,'search.html',context)

def drop(request):
    title="Drop Out"
    form=Sform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = Student.objects.filter(s_name=name).delete()
        if len(queryset)==0:
            return render(request,'ack.html',{'title':'Student Deatils not available Please enter Data'})
        else:
            queryset = Student.objects.filter(s_name=name).delete()
            return render(request,'ack.html',{'title':"Student removed from your database"})
    context={
        'title':title,
        'form':form,
    }
    return render(request,'search.html',context)

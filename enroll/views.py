from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentResgistrations
from .models import User

# this will add and show students


def add_show(request):
    if request.method == 'POST':
        fm = StudentResgistrations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentResgistrations()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

# delete student
def delete_data(request, id):
    if request.method == 'POST':
        d = User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')

# update student

def update_data(request ,id):
    if request.method == "POST":
        d = User.objects.get(pk = id)
        fm = StudentResgistrations(request.POST, instance=d)
        if fm.is_valid():
            fm.save()
    else:
        d = User.objects.get(pk = id)
        fm = StudentResgistrations( instance=d)
    return render(request, "enroll/updatestudent.html", {'form':fm})

#---------CREATE OPERATION----------------
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import sexyform
from . models import sexy
def create(request):
    if request.method=='POST':
        form=sexyform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('read')
    else:
        form=sexyform()
        return render(request,'create.html',{'form':form})    

#-----------READ OPERATION--------------
def read(request):
    obj=sexy.objects.all()
    return render(request,'read.html',{'obj':obj})

#-----------DELETE OPERATION--------------
def delete(request,id):
    obj=sexy.objects.get(id=id)
    obj.delete()
    return redirect('read')

#-----------EDIT OPERATION--------------
def edit(request,id):
    obj=sexy.objects.get(id=id)
    if request.method=='POST':
        fm=sexyform(request.POST,instance=obj)
        if fm.is_valid:
            fm.save()
            return redirect('read')
    else:
        tm=sexyform(instance=obj)
        return render(request,'edit.html',{'tm':tm})    
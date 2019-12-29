from django.shortcuts import render,redirect

# Create your views here.

from .models import Student

def index(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'index.html',context)



def create(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        school=request.POST['school']
        description=request.POST['description']
        newstudent=Student.objects.create(name=name,age=age,school=school,description=description)
        newstudent.save()
        return redirect('index')
    else:
        print(' something is wroing')

    return render(request,'studentform.html',{})
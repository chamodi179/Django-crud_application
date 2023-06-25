from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    data = Student.objects.all()
    context ={"data":data}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def insertData(request):
    data = Student.objects.all()
    context ={"data":data}
    if request.method=="POST":
            name= request.POST.get('name')
            email= request.POST.get('email')
            age= request.POST.get('age')
            gender= request.POST.get('gender')
            query = Student(name=name,email=email,age=age,gender=gender)
            query.save()

    return render(request, 'index.html',context)

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.gender = gender
        edit.age = age
        edit.save()

        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, 'update.html', context)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")


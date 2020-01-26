from django.shortcuts import render,redirect
from students.forms import StudentForm 
from students.models import Student 
# Create your views here.

def index(request):
	students = Student.objects.all()
	return render(request,'students/list.html',{'students':students})

def create(request):
	form = StudentForm()
	return render(request,'students/add.html',{'form':form})

def store(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except Exception as e:
				pass
	return redirect('/students')
			

def edit(request,id):
	return render(request,'students/edit.html')

def update(request,id):
	pass

def destroy(request,id):
	pass

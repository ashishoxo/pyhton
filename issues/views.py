from django.shortcuts import render,redirect
from issues.forms import IssueForm 
from issues.models import Issue 
from students.models import Student 
from books.models import Book 
# Create your views here.

def index(request):
	issues = Issue.objects.all()
	return render(request,'issues/list.html',{'issues':issues})

def create(request):
	form = IssueForm()
	students = Student.objects.all()
	books = Book.objects.all()
	return render(request,'issues/add.html',{'form':form,'students':students,'books':books})

def store(request):
	if request.method == "POST":
		form = IssueForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except Exception as e:
				pass
	return redirect('/issues')
			

def edit(request,id):
	return render(request,'issues/edit.html')

def update(request,id):
	pass

def destroy(request,id):
	pass

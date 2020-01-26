from django.shortcuts import render,redirect
from authors.forms import AuthorForm 
from authors.models import Author 
# Create your views here.

def index(request):
	authors = Author.objects.all()
	return render(request,'authors/list.html',{'authors':authors})

def create(request):
	form = AuthorForm()
	return render(request,'authors/add.html',{'form':form})

def store(request):
	if request.method == "POST":
		form = AuthorForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except Exception as e:
				pass
	return redirect('/authors')
			

def edit(request,id):
	return render(request,'authors/edit.html')

def update(request,id):
	pass

def destroy(request,id):
	pass

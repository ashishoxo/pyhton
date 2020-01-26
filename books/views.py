from django.shortcuts import render, redirect
from books.forms import BookForm 
from books.models import Book 
from authors.models import Author
from django.http import HttpResponse
# Create your views here.

def index(request):
	books = Book.objects.all()
	return render(request,'books/list.html',{'books':books})

def create(request):
	authors = Author.objects.all()
	form = BookForm()
	return render(request,'books/add.html',{'form':form,'authors':authors})

def store(request):
	# return HttpResponse(request.POST.items())
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except Exception as e:
				pass
	return redirect('/books')
			

def edit(request,id):
	return render(request,'books/edit.html')

def update(request,id):
	pass

def destroy(request,id):
	pass
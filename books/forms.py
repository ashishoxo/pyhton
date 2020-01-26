from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
	"""docstring for BookForm"""
	# def __init__(self, arg):
	# 	super(BookForm, self).__init__()
	# 	self.arg = arg
	class Meta:
		model = Book
		fields = "__all__"
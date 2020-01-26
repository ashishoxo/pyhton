from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
	"""docstring for BookForm"""
	# def __init__(self, arg):
	# 	super(BookForm, self).__init__()
	# 	self.arg = arg
	class Meta:
		model = Student
		fields = "__all__"
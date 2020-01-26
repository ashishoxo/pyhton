from django import forms
from issues.models import Issue

class IssueForm(forms.ModelForm):
	"""docstring for BookForm"""
	# def __init__(self, arg):
	# 	super(BookForm, self).__init__()
	# 	self.arg = arg
	class Meta:
		model = Issue
		fields = "__all__"
from django import forms
from authors.models import Author

class AuthorForm(forms.ModelForm):
 	"""docstring for AuthorForm"""
 	# def __init__(self, arg):
 	# 	super(AuthorForm, self).__init__()
 	# 	self.arg = arg
 	class Meta:
 		model = Author
 		fields = "__all__"



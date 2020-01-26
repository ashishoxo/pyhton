from django.db import models

# Create your models here.
class Author(models.Model):
	"""docstring for Author"""
	# def __init__(self, arg):
	# 	super(Author, self).__init__()
	# 	self.arg = arg

	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = "authors"
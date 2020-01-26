from django.db import models
from authors.models import Author

# Create your models here.
class Book(models.Model):
	
	title = models.CharField(max_length = 100)
	cover = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	author = models.ForeignKey(Author,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	isbn = models.CharField(max_length = 100)

	class Meta:
		db_table = "books"
		
from django.db import models
from django_mysql.models import EnumField
from students.models import Student 
from books.models import Book 

# Create your models here.
class Issue(models.Model):
	
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	book = models.ForeignKey(Book,on_delete=models.CASCADE)
	days = models.IntegerField(max_length = 100)
	status = EnumField(choices=['issued','recieved','overdue'])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "issues"
		
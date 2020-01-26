from django.db import models

# Create your models here.
class Student(models.Model):
	
	uid = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)
	father_name = models.CharField(max_length = 200)
	roll_no = models.CharField(max_length = 100)
	current_class = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "students"
		
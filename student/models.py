from django.db import models

# Create your models here.
class Subject(models.Model):
    SubjectNo = models.TextField(unique=True)
    SubjectName = models.TextField()
    SubjectCode = models.TextField()
    SubjectProfessor = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

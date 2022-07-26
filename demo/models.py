from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    total_subjects = models.IntegerField()
    std = models.IntegerField()

    def __str__(self):
        return self.name

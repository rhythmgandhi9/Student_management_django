from django.db import models

class Student(models.Model):
    GRADE_CHOICES = [(str(i), str(i)) for i in range(1, 13)]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)

    def __str__(self):
        return self.name

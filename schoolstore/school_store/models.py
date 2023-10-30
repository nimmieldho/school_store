from django.db import models

# Create your models here.



class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name




class Form(models.Model):
    name = models.CharField(max_length=124)
    Date_of_birth = models.DateField()
    Age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    Phone_Number = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField(max_length=500)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    PURPOSE_CHOICES = [
        ('enquiry', 'Enquiry'),
        ('return', 'Return'),
        ('place_order', 'Place_order'),
        ('FAQ', 'FAQ'),
        ('other', 'Other'),
    ]

    Purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='enquiry')



    def __str__(self):
        return self.name
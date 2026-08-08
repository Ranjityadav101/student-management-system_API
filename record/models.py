from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)   
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"




class Course(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Students,on_delete= models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.DecimalField(
        max_digits=4,decimal_places=2,null= True,blank=True,
        validators= [MinValueValidator(0),MaxValueValidator(100)]
    )


    class Meta:
        unique_together = ('student','course')

        def __str__(self):
            return f"{self.student} - {self.course}"
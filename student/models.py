from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class Stu_Class(models.Model):
    classname=models.CharField(max_length=100)

    def __str__(self):
        return self.classname
class StudentManager(BaseUserManager):
    def create_user(self,phone,password=None,**extra_fields):
        if not phone:
            raise ValueError('Students must have phone number')
        student=self.model(phone=phone,**extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student
    def create_superuser(self,phone,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(phone,password,**extra_fields)
    
class Student_User(AbstractBaseUser):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,unique=True)
    email=models.EmailField(unique=True)
    dateOfBirth=models.DateField()
    status=models.BooleanField(default=False)
    image=models.ImageField(upload_to='media/img',null=True,blank=True)
    cls=models.ForeignKey(Stu_Class,on_delete=models.SET_NULL,null=True)
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=['firstName','lastName','email','dateOfBirth']
    objects=StudentManager()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
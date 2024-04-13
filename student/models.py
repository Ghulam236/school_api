from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin


# Create your models here.
class StuClass(models.Model):
    classname=models.CharField(max_length=100)

    def __str__(self):
        return self.classname
# class StudentManager(BaseUserManager):
#     def create_user(self, phone, password=None, **extra_fields):
#         if not phone:
#             raise ValueError('Students must have a phone number')
#         user = self.model(phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    

#     def create_superuser(self, phone, password **extra_fields):
        
#         user = self.create_user(
#           phone,
#           password=password,
          
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)
        # return self.create_user(phone, password, **extra_fields)
    # def create_user(self,phone,password=None,**extra_fields):
    #     if not phone:
    #         raise ValueError('Students must have phone number')
    #     student=self.model(phone=phone,**extra_fields)
    #     student.set_password(password)
    #     student.save(using=self._db)
    #     return student
    # def create_superuser(self,phone,password,**extra_fields):
    #     extra_fields.setdefault('is_staff',True)
    #     extra_fields.setdefault('is_superuser',True)
    #     if not extra_fields.get('is_staff'):
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if not extra_fields.get('is_superuser'):
    #         raise ValueError('Superuser must have is_superuser=True.')

    #     return self.create_user(phone,password,**extra_fields)
    # def _create_user(self, phone, password, **extra_fields):
    #     """Create and save a User with the given phone and password."""
    #     if not phone:
    #         raise ValueError('The given phone must be set')
    #     user = self.model(phone=phone, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_user(self, phone, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(phone, password, **extra_fields)

    # def create_superuser(self, phone, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)

    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')

        # return self._create_user(phone, password, **extra_fields)
class StudentUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, phone, password,email,dateOfBirth, **extra_fields):
        if not phone:
            raise ValueError(_('Users must have an phone number'))
       
        user = self.model(phone=phone,email=email,dateOfBirth=dateOfBirth, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)
class StudentUser(AbstractBaseUser):
    phone=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    dateOfBirth=models.DateField(null=True, blank=True)
    image=models.ImageField(upload_to='images',null=True,blank=True)
    cls=models.ForeignKey(StuClass,on_delete=models.SET_NULL,null=True)
    is_staff = models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    username=None
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]
    objects=StudentUserManager()

    def __str__(self):
        return f"{self.phone}"
    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?
        return True



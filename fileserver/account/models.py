from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,date_of_birth=None,password=None):
        if not username:
            raise ValueError("You must provide your username")
        if not email:
            raise ValueError("You must provide your email")
        user = self.model(
            username= username,
            email = self.normalize_email(email),
            date_of_birth = date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,date_of_birth=None,password=None):
        user = self.create_user(username=username,email=email,
                                date_of_birth=date_of_birth,password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name='User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

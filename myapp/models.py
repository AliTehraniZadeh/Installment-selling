from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser #برای ساخت کاربر دلخواه
from django.core.validators import RegexValidator
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, user_name, password=None):

        if not user_name:
            raise ValueError("Users must have an user_name")

        user = self.model(user_name = user_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password):
        """
        Creates and saves a superuser with the given user_name and password.
        """
        user = self.create_user(user_name,password)
        user.is_superuser = True
        user.is_staff = True #از کاربران ادمین است
        user.set_password(password) # پسوورد کاربر را هش می کند
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=50,unique=True, null= True)
    first_name = models.CharField(max_length = 50 , null = True)
    last_name = models.CharField(max_length = 50 , null = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_name
    

class ShopModel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    branch = models.ForeignKey('BranchModel',related_name='branch', on_delete= models.CASCADE, null= True, blank= True)
    address = models.TextField(default='Iran')
   
    def __str__(self):
        return self.name
    

class BranchModel(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE)
    address = models.TextField(default='Iran')
    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=1)
    price = models.FloatField()
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.name


class CheckModel(models.Model):
    serial_number = models.CharField(max_length = 16, unique = True, validators=[
            RegexValidator(regex='^[0-9]*$',
            message='فرمت شماره سریال رعایت نشده است',
            code='invalid_serial_number')])
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product', default=1)
    amount = models.FloatField()
    bank = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.serial_number


class InstallmentModel(models.Model):
    installment_check = models.ForeignKey(CheckModel, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    Issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.due_date ,'is due date'
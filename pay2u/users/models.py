from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, phone, email, password):
        if not phone:
            raise ValueError("У пользователя должен быть номер телефона")
        if not email:
            raise ValueError("У пользователя должен быть email")
        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            password=password,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password=None):
        if password is None:
            raise ValueError("Пароль не может быть пустым")
        user = self.create_user(
            phone=phone,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField("Номер телефона", max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.phone

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
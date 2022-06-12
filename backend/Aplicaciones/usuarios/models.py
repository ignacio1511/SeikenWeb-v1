from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, first_name, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=Truimage.pnge.")

        return self.create_user(email, first_name, password, **other_fields)

    def create_user(self, email, first_name, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    code = models.AutoField(_("id"), primary_key=True)
    email = models.EmailField(_("email address"), null=False, unique=True)
    username = models.CharField(max_length=40, blank=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    objetivos_fitness = [
        ("perder_grasa", "Quiero bajar de peso lo antes posible"),
        ("ganar_musculo", "Quiero ganar músculo aceleradamente"),
        ("ambos", "Quiero definir mi cuerpo"),
    ]
    objetivo = models.CharField(choices=objetivos_fitness, max_length=50, null=False)

    niveles = [
        ("1", "Nivel 1: soy un Seiken iniciando con todo"),
        ("2", "Nivel 2: +15 planchas y 5 dominadas"),
        ("3", "Nivel 3: +5 planchas una mano y +10 dominadas"),
    ]
    nivel = models.CharField(_("Nivel"), choices=niveles, max_length=350, null=False)

    start_date = models.DateTimeField(auto_now_add=True)
    about = models.TextField(_("about"), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "objetivo"]

    def __str__(self):
        return self.email

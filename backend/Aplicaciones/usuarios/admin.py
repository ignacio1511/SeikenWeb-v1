from Aplicaciones.usuarios.models import NewUser
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import CharField, Textarea, TextInput



class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "objetivo",
    )
    list_filter = ("email", "first_name", "last_name", "objetivo", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = ("email", "first_name", "last_name", "objetivo", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "objetivo",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Personal", {"fields": ("about",)}),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name","last_name","objetivo","password1", "password2", "is_active", "is_staff"),
            },
        ),
    )



admin.site.register(NewUser, UserAdminConfig)

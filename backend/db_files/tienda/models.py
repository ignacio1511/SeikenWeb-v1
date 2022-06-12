# from django.db import models
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _
# from mptt.models import MPTTModel, TreeForeignKey


# class Category(MPTTModel):
#     """
#     Category Table implimented with MPTT.
#     """

#     name = models.CharField(
#         verbose_name=_("Category Name"),
#         help_text=_("blank and unique"),
#         max_length=255,
#         unique=True,
#     )
#     slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
#     parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
#     is_active = models.BooleanField(default=True)

#     class MPTTMeta:
#         order_insertion_by = ["name"]

#     class Meta:
#         verbose_name = _("Category")
#         verbose_name_plural = _("Categories")

#     def get_absolute_url(self):
#         return reverse("Aplicaciones.plataforma:category_list", args=[self.slug])

#     def __str__(self):
#         return self.name


# class Country(models.Model):
#     country_id = models.PositiveIntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     continet_name = models.CharField(max_length=50, blank=False)


# class Product(models.Model):
#     product_id = models.PositiveIntegerField(primary_key=True)
#     name = models.CharField(max_length=50, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=False)
#     price = models.PositiveIntegerField(blank=True)
#     product_type = models.CharField(max_length=100, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=False)


# class User(models.backend):
#     user_id = models.AutoField(primary_key=True)
#     full_name = models.CharField(max_length=100, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=False)
#     country_code = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, symmetrical=False)

#     fitness_goals = [
#         ("perder_grasa", "Quiero bajar de peso y quemar grasa rusuariosdo"),
#         ("ganar_musculo", "Soy muy flaco y quiero aumentar mi masa muscular"),
#         ("ambos", "Quiero tonificar y verme mas marcado"),
#     ]

#     fitness_goal = models.CharField(max_length=200, choices=fitness_goals)

#     class Meta:
#         verbose_name = _("NewUser")
#         verbose_name_plural = _("NewUsers")

#     def __str__(self):
#         return self.name


# class OrderItem(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
#     qunatity = models.PositiveIntegerField(blank=False)


# class Order(models.Model):
#     order_id = models.ForeignKey(OrderItem, null=False, blank=False, on_delete=models.CASCADE)
#     user_id = models.PositiveIntegerField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=False)


# class ProductImage(models.Model):
#     """
#     The Product Image table.
#     """

#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
#     image = models.ImageField(
#         verbose_name=_("image"),
#         help_text=_("Upload a product image"),
#         upload_to="images/",
#         default="images/default.png",
#     )
#     alt_text = models.CharField(
#         verbose_name=_("Alturnative text"),
#         help_text=_("Please add alturnative text"),
#         max_length=255,
#         null=True,
#         blank=True,
#     )
#     is_feature = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True)

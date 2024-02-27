from django.contrib import admin
from .models import User,Product,ProductImage
# Register your models here.
admin.site.register(User)
admin.site.register(ProductImage)
admin.site.register(Product)
from django.contrib import admin
from .models import ProductImg, Category, Product


# Register your models here.

class ProductImgInlane(admin.StackedInline):
    model= ProductImg


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInlane]


admin.site.register(Category)

admin.site.register(Product,ProductAdmin)



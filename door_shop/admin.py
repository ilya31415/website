from django.contrib import admin

from door_shop.models import Product, Order, ProductOrder, Categories, CategoriesProduct, Client


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 1


class CategorisProductInline(admin.TabularInline):
    model = CategoriesProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "image", "display_categories_name"]
    inlines = [CategorisProductInline, ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["create_at", "client", "order_cost"]
    inlines = [ProductOrderInline, ]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "display_products_name"]
    inlines = [CategorisProductInline]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "phoneNumber"]

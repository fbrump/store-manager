from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"

    list_display = ["code", "name", "price", "price_currency", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active", "price_currency"]
    list_per_page = 50
    ordering = ["name", "created_at",]
    
    search_fields = ["name", "code",]
    exclude = ["created_at", "updated_at", "created_by"]
    fields = [
        ("code","name"),
        ("price_currency","price"),
        "is_active",
        ("created_at", "updated_at", "created_by",),]
    readonly_fields = ["created_at", "updated_at", "created_by"]
    def save_model(self, request, obj, form, change):
        if (not change):
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)

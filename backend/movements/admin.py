from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"

    list_display = ["product", "amount", "type", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active", "type"]
    list_per_page = 50
    ordering = ["-created_at",]
    
    search_fields = ["product",]
    exclude = ["created_at", "updated_at", "created_by"]
    fields = [
        "product",
        ("type", "amount",),
        "is_active",
        ("created_at", "updated_at", "created_by",),]
    readonly_fields = ["created_at", "updated_at", "created_by"]
    def save_model(self, request, obj, form, change):
        if (not change):
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Transaction, TransactionAdmin)

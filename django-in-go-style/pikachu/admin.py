from django.contrib import admin
from pikachu.models import Pikachu

# Register your models here.
@admin.register(Pikachu)
class PikachuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_admin",
        "age",
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"
    ordering = ["updated_at"]
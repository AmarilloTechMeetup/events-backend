from captcha_admin import admin
from django.contrib import admin as a
from .models import *


class ContentAdmin(a.ModelAdmin):
    list_display = ['purpose', 'title', 'posted']
    ordering = ['posted']

class CategoryAdmin(a.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(Content, ContentAdmin)
admin.site.register(Category, CategoryAdmin)


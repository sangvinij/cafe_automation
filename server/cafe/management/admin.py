from django.contrib import admin

from .models import CafeAddresses, Category, Menu, SocialMediaLinks


admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(SocialMediaLinks)
admin.site.register(CafeAddresses)

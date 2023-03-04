from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User, Cart, CartItems


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', 'first_name')

    def clean_password(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password1")
        return password

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('first_name', 'phone_number', 'is_superuser')
    list_filter = ('is_superuser', 'is_staff')
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password'),
        }),
    )
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('first_name', 'phone_number')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Cart)
admin.site.register(CartItems)

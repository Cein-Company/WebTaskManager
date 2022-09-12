from django.contrib import admin
from .models import NewUser

# Register your models here.


class NewUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'password', 'passrepeat')


admin.site.register(NewUser, NewUserAdmin)

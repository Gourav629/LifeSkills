from django.contrib import admin
from blog.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    """This is the admin interface """
    readonly_fields = ['img_preview']
    list_display = ('img_preview','u_id', 'name', 'email', 'text')


admin.site.register(User,UserAdmin)     # register
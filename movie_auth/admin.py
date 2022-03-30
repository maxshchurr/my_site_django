from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as DjangoUser
# from .models import User
from .models import Site_User

class UserInLine(admin.StackedInline):
    model = Site_User
    can_delete = False
    verbose_name_plural = 'users'


class UserAdmin(BaseUserAdmin):
    inlines = (UserInLine, )


admin.site.unregister(DjangoUser)

admin.site.register(Site_User)
# admin.site.register(UserAdmin)
from django.contrib import admin
from app1.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email',)


admin.site.register(Profile,ProfileAdmin)

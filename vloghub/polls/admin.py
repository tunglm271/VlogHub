from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,vlog,ProfileInfor
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

#admin.site.register(Profile)
admin.site.unregister(User)

admin.site.register(User,UserAdmin)
admin.site.register(vlog)
admin.site.register(ProfileInfor)
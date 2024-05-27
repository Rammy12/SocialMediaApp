from django.contrib import admin
from .models import User,UserFollow,UserProfileImage




class ShowId(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User, ShowId)
admin.site.register(UserFollow,ShowId)
admin.site.register(UserProfileImage,ShowId)
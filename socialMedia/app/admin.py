from django.contrib import admin
from .models import User,UserFollow




class ShowId(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User, ShowId)
admin.site.register(UserFollow,ShowId)
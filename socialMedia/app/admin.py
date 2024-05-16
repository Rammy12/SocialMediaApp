from django.contrib import admin
from .models import User




class ShowId(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User, ShowId)
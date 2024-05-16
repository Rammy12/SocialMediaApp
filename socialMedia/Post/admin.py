from django.contrib import admin
from .models import Post,PostLike




class ShowId(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Post, ShowId)
admin.site.register(PostLike, ShowId)

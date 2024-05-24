from django.contrib import admin
from .models import Post,PostLike,postComment




class ShowId(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Post, ShowId)
admin.site.register(PostLike, ShowId)
admin.site.register(postComment,ShowId)

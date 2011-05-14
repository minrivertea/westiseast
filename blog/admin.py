from westiseast.blog.models import Photo, BlogEntry, CoolShit
from django.contrib import admin

class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('date_added', 'title', 'is_draft')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_img', 'title')

admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(CoolShit)

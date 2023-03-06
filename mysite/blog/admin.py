from django.contrib import admin
from .models import Blog
from django.utils import timezone

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    def is_recently_published(self, admin_obj):
        if admin_obj.is_published:
            published_date = admin_obj.date_of_release
            present_date = timezone.now()
            recent_date = present_date - timezone.timedelta(days= 7) 
            if published_date > recent_date:
                return True
            else:
                return False

    list_display = ["title", "author", "description", "is_published", "is_recently_published"]
    list_filter = ['is_published']
    search_fields = ['title']



admin.site.register(Blog, BlogAdmin)
from django.contrib import admin
from .models import Experience
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Experience,ArticleAdmin)
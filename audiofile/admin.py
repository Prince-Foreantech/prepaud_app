from django.contrib import admin

# Register your models here.
from .models import category,subcategory,audiofile

admin.site.register(category)
admin.site.register(subcategory)

@admin.register(audiofile)
class AudiofileAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinymedia.js',)
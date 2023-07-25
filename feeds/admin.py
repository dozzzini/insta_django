from django.contrib import admin
from .models import Feed

# Register your models here.
@admin.register(Feed)
class Feed(admin.ModelAdmin):
    list_display=("caption", "contentImg", "likesNum",)
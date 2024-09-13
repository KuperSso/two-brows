from django.contrib import admin
from .models import Welcome
from .models import Diplomas

@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title', )

@admin.register(Diplomas)
class DiplomasAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id', 'title')


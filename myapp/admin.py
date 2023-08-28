from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AppBar, Portell, Landing, Body, Contact, Message

@admin.register(AppBar)
class AppBarAdmin(admin.ModelAdmin):
    list_display = ['home', 'about', 'wines', 'contact']
    list_display_links = ['home']
    search_fields = ['home', 'about', 'wines', 'contact']

@admin.register(Portell)
class PortellAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'alcohol', 'variety', 'display_image']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'type', 'alcohol', 'variety']
    list_filter = ['type']

    def display_image(self, obj):
        return obj.image.url if obj.image else ''
    
    display_image.short_description = 'Image'


@admin.register(Landing)
class LandingAdmin(admin.ModelAdmin):
    list_display = ['text', 'caption']
    list_display_links = ['text']
    search_fields = ['text', 'caption']

@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    list_display_links = ['title']
    search_fields = ['title', 'text']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']
    search_fields = ['title', 'description']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['first', 'second', 'third', 'fourth']
    search_fields = ['first', 'second', 'third', 'fourth']



from django.contrib import admin
from .models import Puppy, Offer, Contact, Images, PostCategory, BlogPost, BlogImages, Appointment, Newsletter
# Register your models here.



class PuppyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, PuppyAdmin)
admin.site.register(Puppy, PuppyAdmin)
admin.site.register((Offer, Contact, Images, PostCategory, BlogImages, Appointment, Newsletter))
from django.contrib import admin
from .models import Breed, Puppy, Offer, Contact, Images
# Register your models here.



class PuppyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Puppy, PuppyAdmin)
admin.site.register((Breed, Offer, Contact, Images))
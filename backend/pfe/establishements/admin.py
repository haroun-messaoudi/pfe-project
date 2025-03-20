from django.contrib import admin
from .models import Establishement, Images


class ImageInline(admin.TabularInline):
    model = Images
    extra = 1 

# Custom admin for the Establishement model
class EstablishementAdmin(admin.ModelAdmin):
    inlines = [ImageInline] 

# Register the Establishement model with the custom admin
admin.site.register(Establishement, EstablishementAdmin)
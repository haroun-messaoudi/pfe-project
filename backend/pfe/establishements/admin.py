from django.contrib import admin
from .models import Establishement, Images, Amenity, Hotel,Restaurant,Room,Table,MenuItem,Cuisine


class ImageInline(admin.TabularInline):
    model = Images
    extra = 1 

# Adding the images within the establishement table in the admin panel
class EstablishementAdmin(admin.ModelAdmin):
    inlines = [ImageInline] 

# Register the Establishement model with the custom admin
admin.site.register(Establishement, EstablishementAdmin)
admin.site.register(Images)
admin.site.register(Amenity)
admin.site.register(Hotel)
admin.site.register(Restaurant)
admin.site.register(Room)
admin.site.register(Table)
admin.site.register(MenuItem)
admin.site.register(Cuisine)
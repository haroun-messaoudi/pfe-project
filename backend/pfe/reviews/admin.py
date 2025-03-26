from django.contrib import admin
from .models import Review,ReviewAnswer,ReviewQuestion
# Register your models here.

admin.site.register(Review)
admin.site.register(ReviewAnswer)

admin.site.register(ReviewQuestion)
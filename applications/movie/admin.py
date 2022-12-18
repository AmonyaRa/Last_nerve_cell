from django.contrib import admin

# Register your models here.
from applications.movie.models import *

admin.site.register(Review)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Like)
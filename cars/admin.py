from django.contrib import admin

from .models import CarDetails, CarImage, CarMake

# Register your models here.


class CarDetailsAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina', 'image_tag', 'skelbimasSukurtas', 'prekyboje')

admin.site.register(CarDetails, CarDetailsAdmin)


#admin.site.register(CarDetails)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('selected_car', 'alt_text', 'image_tag')

admin.site.register(CarImage, CarImageAdmin)

admin.site.register(CarMake)




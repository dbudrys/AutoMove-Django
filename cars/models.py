from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from django.shortcuts import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.



class CarMake(models.Model):
    # Title
    car_make = models.CharField(max_length=200,  verbose_name='Car Make')

    # Must be returned as string
    def __str__(self):
        return str(self.car_make)
    # # Give it a proper table name in Django Admin Panel
    class Meta:
        verbose_name_plural = "Car Make" 






# Creating Car Details properties
class CarDetails(models.Model):
    
    # Car Make
    automobilio_marke = models.ForeignKey(CarMake, related_name='automobilio_marke_name', on_delete=models.DO_NOTHING, verbose_name='Automobilio Markė')
    
    # Title
    pavadinimas = models.CharField(max_length=200, null=False, blank=True)
    
    # Main Car Image  
    image = models.ImageField('Pragrindine_Nuotrauka', blank=True, default='/car_images/default.png')

    # Thumbnail Image
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(387, 275)], format='JPEG', options={'quality': 90})


    # Car Cost
    kaina = models.IntegerField(null=False, blank=True)

    # MakeYear 
    pagaminimoMetai = models.IntegerField(null=False, blank=True)
     
    # MakeMonth
    MONTH_CHOICES = (
        ('', ''),
        ('-01', '01'),
        ('-02', '02'),
        ('-03', '03'),
        ('-04', '04'),
        ('-05', '05'),
        ('-06', '06'),
        ('-07', '07'),
        ('-08', '08'),
        ('-09', '09'),
        ('-10', '10'),
        ('-11', '11'),
        ('-12', '12'),
    )
    pagaminimoMenuo = models.CharField(max_length=25, choices=MONTH_CHOICES, null=True ,default='',)   

    # Mileage
    rida = models.IntegerField(null=False, blank=True)

    # Engine
    variklis = models.CharField(max_length=255, null=False, blank=True)

    # FuelType
    FUEL_CHOICES = (
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
    )
    kuroTipas = models.CharField(max_length=25, choices=FUEL_CHOICES, default='Benzinas',)

    # CarType - Car body types
    TYPE_CHOICES = (
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Station Wagon', 'Station Wagon'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Minivan', 'Minivan'),
        ('Other', 'Other'),
    )
    kebuloTipas = models.CharField(max_length=25, choices=TYPE_CHOICES, default='Sedan',)
    
    # Drive Type
    varantisRatai = models.CharField(max_length=100, null=False, default='FWD')


    # Transmission
    TRANSMISSION_CHOICES = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )
    pavaruDeze = models.CharField(max_length=25, choices=TRANSMISSION_CHOICES, default='Manual',)

    
    #Color
    spalva = models.CharField(max_length=50, null=True, blank=True)

    # Issues
    defektai = models.CharField(max_length=100, null=True, default='Nothing')
    
    # Post Created - Time 
    skelbimasSukurtas = models.DateTimeField(default = datetime.now, blank = True)


    # Additional Info - Detailed Description
    komentarai = models.TextField(null=True, blank=True)

    # Selling/Sold/NotSpecified
    SALE_CHOICES = (
        ('Parduodama', 'Selling'),
        ('Parduota', 'Sold'),
        ('Rezervuota', 'Reserved'),
        ('Kita', 'Other'),
    )
    prekyboje = models.CharField("Prekyboje?", max_length=10, choices=SALE_CHOICES, default='Parduodama',)




    # Pirmosios registracijos salis
    # Defektai - poro zodziu
    # Varantis ratai

    # Ratlankius issimti
    # Techaapziura 


    # Set proper field name in Django Admin Panel
    def __str__(self):
        return self.pavadinimas
    # Give it a proper table name in Django Admin Panel
    class Meta:
        verbose_name_plural = "Car Description" 

    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 100px; height:80px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    # Used to return URL of each car for sitemap.xml
    def get_absolute_url(self):
        car_details_url = '/cars/' + str(self.id)

        return car_details_url



class CarImage(models.Model):
    selected_car = models.ForeignKey(CarDetails, related_name='selected_car_name', on_delete=models.CASCADE, verbose_name='Pasirinkti_Automobili')
    
    car_image = models.ImageField(upload_to='car_images/', blank=True, null=False, verbose_name='Pasirinkti_Nuotrauka')

   
    ALT_TEXT_CHOICES = (
        ('Front', 'Front'),
        ('Back', 'Back'),
        ('Side', 'Side'),
        ('Inside', 'Inside'),
        ('Paperwork', 'Paperwork'),
        ('Other', 'Other'),
    )

    alt_text = models.CharField(max_length=200, null=True,  choices=ALT_TEXT_CHOICES, default='Kita', verbose_name='Papildomas_Tekstas')


    # Must be returned as string
    def __str__(self):
        return str(self.selected_car)
    # # Give it a proper table name in Django Admin Panel
    class Meta:
        verbose_name_plural = "Car Images" 

    def image_tag(self):
        if self.car_image:
            return mark_safe('<img src="%s" style="width: 75px; height:50px;" />' % self.car_image.url)
        else:
            return 'No Image Found'
    
        image_tag.short_description = 'Image'





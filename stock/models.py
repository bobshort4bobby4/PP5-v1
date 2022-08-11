'''
   define models for stock app
'''


from django.db import models


class Maker(models.Model):
    """
    Define Maker relation structure
    """
    Maker_Types = (
        ('Bmw', 'Bmw'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Toyota', 'Toyota'),
        ('Nissan', 'Nissan'),
        ('Mazda', 'Mazda'),
        ('Mercedes', 'Mercedes'),
    )

    maker = models.CharField(max_length=10, null=False, choices=Maker_Types)

    def __str__(self):
        return f'{self.maker}'

    objects = models.Manager()


class FuelType(models.Model):
    '''
    Define types of fuel choices
    '''

    Fuel_Types = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    )

    fuel = models.CharField(max_length=15, null=False, choices=Fuel_Types)

    def __str__(self):
        return f'{self.fuel}'

    objects = models.Manager()


class Vehicle(models.Model):
    """
    Define Vehicle relation structure
    """
    stock_num = models.AutoField(primary_key=True, editable=False)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    model = models.CharField(max_length=20, null=False)
    year = models.IntegerField(null=False)
    fuel = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    featured = models.BooleanField(default=True)
    preowned = models.BooleanField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    odometer = models.IntegerField()
    colour = models.CharField(max_length=25)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.maker}, {self.model}'

    objects = models.Manager()

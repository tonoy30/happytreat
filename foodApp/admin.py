from django.contrib import admin
from .models import Profile, FoodRequest, DonatedFood
# Register your models here.
admin.site.register(Profile)
admin.site.register(FoodRequest)
admin.site.register(DonatedFood)

from django.contrib import admin
from restaurants.models import Restaurant, Food, OrderMain, OrderDetail

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(OrderMain)
admin.site.register(OrderDetail)

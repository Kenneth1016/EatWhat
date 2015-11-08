from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    restaurant = models.ForeignKey(Restaurant)
    memo = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name

class OrderMain(models.Model):
    orderDate = models.DateField()
    createId = models.CharField(max_length=20)
    createAt = models.DateField()
    restaurant = models.ForeignKey(Restaurant)
    valid = models.BooleanField(default=True)
    orderable = models.BooleanField(default=True)
    memo = models.CharField(max_length=200, blank=True)
    orderDueDate = models.DateTimeField(blank=True)


class OrderDetail(models.Model):
    orderMain = models.ForeignKey(OrderMain)
    createId = models.CharField(max_length=20)
    createAt = models.DateField()
    valid = models.BooleanField(default=True)
    food = models.ForeignKey(Food)
    memo = models.CharField(max_length=200, blank=True)
    isPaid = models.BooleanField(default=False)
    money = models.DecimalField(max_digits=5, decimal_places=0)


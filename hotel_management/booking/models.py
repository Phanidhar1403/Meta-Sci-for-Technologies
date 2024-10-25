from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    floor_number = models.IntegerField()
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"

class FoodOrder(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Order for {self.booking.customer_name} - {self.food_item}"


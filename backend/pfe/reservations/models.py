from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import Profile
from establishements.models import Table,Room
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
class HotelReservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    RESERVATION_TYPE_CHOICES = [
        ('quick', 'Quick'),
        ('normal', 'Normal'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reservation_type = models.CharField(max_length=20, choices=RESERVATION_TYPE_CHOICES, default='normal')

    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(1)])


    room = models.ForeignKey('establishements.Room', on_delete=models.CASCADE)
    guest = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #was_confirmed = models.BooleanField(default=False , editable=False)
    def confirm(self):
        self.status = 'confirmed'
        self.save()

    def cancel(self):
        self.status = 'cancelled'
        self.save()

    def clean(self):
        super().clean()

        if self.check_in_date and self.check_out_date:
            if self.check_in_date >= self.check_out_date:
                raise ValidationError({
                    'check_out_date': 'Check-out date must be after check-in date.'
                })

        if self.room and self.number_of_people > self.room.capacity:
            raise ValidationError({
                'number_of_people': 'Number of people exceeds room capacity.'
            })

        # Optional: Check overlapping reservations for same room
        overlapping = HotelReservation.objects.filter(
            room=self.room,
            status__in=['pending', 'confirmed'],
            check_out_date__gt=self.check_in_date,
            check_in_date__lt=self.check_out_date
        ).exclude(pk=self.pk)
        if overlapping.exists():
            raise ValidationError("This room is already booked for the selected dates.")

    def save(self, *args, **kwargs):
        # track previous confirmation state
        if self.pk:
            orig = HotelReservation.objects.get(pk=self.pk)
            self.was_confirmed = (orig.status == 'confirmed')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.guest.user.username} revervation at {self.room.hotel}"

class RestaurantReservation(models.Model) :

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',)
    date = models.DateTimeField()
    numberOfPeople = models.IntegerField(validators=[MinValueValidator(1)])##max value needed look for it
    ReservationType = [('quick','Quick'),('normal','Normal')]


    table = models.ForeignKey(Table , on_delete=models.CASCADE)
    guest = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest.user.username} revervation at {self.table.restaurant}"
    def confirm(self):
        self.status = 'confirmed'
        self.save()

    def cancel(self):
        self.status = 'cancelled'
        self.save()









# @receiver(post_save, sender=HotelReservation)
# def handle_reservation_status_change(sender, instance, created, **kwargs):
#     just_confirmed = instance.status == 'confirmed' and not instance.was_confirmed
#     if just_confirmed:
#         # 1) block inventory now
#         decrement_available_rooms.delay(instance.room_id)

#         # 2) schedule inventory release at checkout
#         eta = datetime.datetime.combine(
#             instance.check_out_date,
#             datetime.time.min,
#             tzinfo=timezone.get_current_timezone()
#         )
#         increment_available_rooms.apply_async((instance.room_id,), eta=eta)
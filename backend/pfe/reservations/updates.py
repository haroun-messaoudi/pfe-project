# # tasks.py
# from celery import shared_task
# from django.db.models import F

# @shared_task
# def decrement_available_rooms(room_id):
#     from .models import Room
#     Room.objects.filter(id=room_id).update(available_rooms=F('available_rooms') - 1)

# @shared_task
# def increment_available_rooms(room_id):
#     from .models import Room
#     Room.objects.filter(id=room_id).update(available_rooms=F('available_rooms') + 1)

from django.shortcuts import render, redirect
from .models import Room, Booking
from django.contrib import messages


def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'booking/room_list.html', {'rooms': rooms})


def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']

        booking = Booking.objects.create(
            customer_name=customer_name,
            room=room,
            check_in_date=check_in,
            check_out_date=check_out,
            total_price=room.price,
        )

        room.is_available = False
        room.save()

        messages.success(request, 'Room booked successfully!')
        return redirect('room_list')

    return render(request, 'booking/book_room.html', {'room': room})

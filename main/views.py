from django.shortcuts import render

from . import models

import datetime as dt


def index(request):
    return render(request, 'index.html', {'current_page': 'index'})


def room(request):
    return render(request, 'room.html', {'current_page': 'room'})


def room_reserv(request, id):
    if request.method == 'GET':
        return render(request, 'room_reserv.html', {'id': id})
    
    context = {
        'id': id,
        'datefrom': request.POST.get('datefrom'),
        'dateto': request.POST.get('dateto'),
    }
    
    datefrom = dt.date.fromisoformat(request.POST['datefrom'])
    dateto = dt.date.fromisoformat(request.POST['dateto'])
    
    reservations = models.RoomReservation.objects.filter(room=id)
    items = []
    for item in reservations:
        if datefrom < item.date < dateto:
            items.append(item)
            
    if len(items) > 0:
        context['items'] = ', '.join(item.date.strftime("%m.%d.%Y") for item in items)
        context['success'] = False
        return render(request, 'room_reserv.html', context)

    temp = dt.date.fromisoformat(request.POST['datefrom'])
    for i in range((dateto - datefrom).days):
        models.RoomReservation.objects.create(room=id, date=temp).save()
        temp += dt.timedelta(days=1)
    
    context['success'] = True
    return render(request, 'room_reserv.html', context)
    


def faq(request):
    return render(request, 'faq.html', {'current_page': 'faq'})

from django.shortcuts import render
from .models import Route, Station


def bus_stations(request):
    context = dict()
    context['routes'] = Route.objects.all()
    route = request.GET.get('route')
    if route:
        route = Route.objects.get(name=route)
        context['stations'] = route.stations.all()
        lat = [lat.latitude for lat in context['stations']]
        y = round((sum(lat) / len(lat)), 8)
        long = [long.longitude for long in context['stations']]
        x = round((sum(long) / len(long)), 8)
        context['center'] = {'x': x, 'y': y}
    return render(request,
                  'stations.html',
                  context)


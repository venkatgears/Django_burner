from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {"id" : 1 , "name" : "room1"},
    {"id" : 2 , "name" : "room2"},
    {"id" : 3 , "name" : "room3"},
    {"id" : 4 , "name" : "room4"}
]

def Home(request):
    context = {"rooms" : rooms}
    return render(request, 'base/home.html', context=context)

def Rend(request,pk):
    print(pk, type(pk))
    room = {}
    for i in rooms:
        if i['id'] == int(pk) :
            room = i
    context =  room
    print(context)
    return render(request,"base/room.html", context)
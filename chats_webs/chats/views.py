from django.shortcuts import render,redirect,get_object_or_404
# from django.http import JsonResponse
from django.contrib.auth import get_user
from .models import Message
import json
# Create your views here.
def sala_chats(req,sala):
    return render(req,'salas/plantilla_sala.html')

def lobby_salas(req):
    if req.method == 'GET':
        if req.GET.get('room_name'):
            return redirect(f'../sala/{req.GET.get("room_name")}')
    return render(req,'salas/lobby_salas.html')

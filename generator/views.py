from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def password(request):

    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    special_characters = request.GET.get('special')
    numbers = request.GET.get('numbers')

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    if uppercase == 'on':
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if special_characters == 'on':
        characters.extend(list('!@#$%^&*()'))

    if numbers == 'on':
        characters.extend(list('0123456789'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password': generated_password})

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def anusri(request):
    return HttpResponse('<h1>she is daughter of suneethamahesh</h1>')
def venky(request):
    return HttpResponse('<h1>he is son of ramanamma</h1>')

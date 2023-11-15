from nz.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('anusri/',anusri,name='anusri'),
    path('venky/',venky,name='venky'),
]   
from django.urls import path
from .views import salom,kursant,guruh



urlpatterns=[
    path('', salom, name= "salomlashish"),
    path('kursantyubor/', kursant, name= "kursant"),
    path('kursantyubor/<int:pk>/', kursant, name= "kursantlar"),
    path('guruhyubor/', guruh, name= "guruh"),
    path('guruhyubor/<int:pk>/', guruh, name= "guruhlar")
]
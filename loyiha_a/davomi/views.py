from django.shortcuts import render, HttpResponse
from .models import Guruhlar,Kursantlar

# Create your views here.
def salom(requests):
    return render(requests, 'index.html', {})


def kursant(requests, pk=None):
    if pk:
        root= Kursantlar.objects.get(pk=pk)
        ctx = {
            'root': root
        }
    else:
        kursantcha= Kursantlar.objects.all()
        ctx={
        'kursantcha':kursantcha
    }

    return render(requests, 'kursant.html', ctx)

def guruh(requests, pk=None):
    if pk:
        root=Kursantlar.objects.all().filter(guruh_id=pk)
        ctx={
            'root':root
        }
    else:
        guruhcha=Guruhlar.objects.all()
        ctx={
            'guruhcha':guruhcha
        }
    return render(requests, 'guruh.html', ctx)


from django.shortcuts import render
from django.http import HttpResponse
from.models import movies
from math import ceil
# Create your views here.
def index(request):
    movie=movies.objects.all()
    print(movie)
    n=len(movie)
    nSlides= n//7 + ceil((n/7)-(n//7))
    params={"movie":movie,"slides":nSlides,"range":range(1,nSlides)}
    return render(request,'index.html',params)
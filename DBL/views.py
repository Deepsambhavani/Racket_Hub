from django.shortcuts import render
from .models import rackets , racket_reviews , racket_type , LaserSerial
from django.shortcuts import get_object_or_404
from .forms import racketform
# Create your views here.
def DBl(request):
    all_rackets = rackets.objects.all()
    return render(request, 'DBL/DBL.html', {'rackets': all_rackets})
def buy_racket(request, racket_id):
    racket = get_object_or_404(rackets, pk= racket_id)
    
    return render(request, 'DBL/buy.html', {'racket': racket  } )

def all_rackets(request):
    stores = None
    if request.method == 'POST':
        form = racketform(request.POST)
        if form.is_valid():
            chosen_racket = form.cleaned_data['racket_type']
            stores = chosen_racket.types.all()  
    else:
        form = racketform()
    return render(request, 'DBL/all_rackets.html', {'rackets': stores, 'form': form})
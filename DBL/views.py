from django.shortcuts import redirect, render
from .models import rackets , racket_reviews , racket_type , LaserSerial
from django.shortcuts import get_object_or_404
from .forms import ReviewForm, racketform
# Create your views here.
def DBl(request):
    all_rackets = rackets.objects.all()
    return render(request, 'DBL/DBL.html', {'rackets': all_rackets})
def buy_racket(request, racket_id):
    racket = get_object_or_404(rackets, id=racket_id)
    reviews = racket.reviews.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.racket = racket 
            new_review.save()
            return redirect('view_racket', racket_id=racket.id)
    else:
        form = ReviewForm()
        
    context = {
        'racket': racket,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'DBL/buy.html', context)
def all_rackets(request):
    stores = None
    if request.method == 'POST':
        form = racketform(request.POST)
        if form.is_valid():
            chosen_racket = form.cleaned_data['racket_type']
            stores = chosen_racket.rackets.all()  
    else:
        form = racketform()
    return render(request, 'DBL/all_rackets.html', {'rackets': stores, 'form': form})
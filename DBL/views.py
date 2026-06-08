from django.shortcuts import redirect, render
from .models import rackets, racket_reviews, racket_type, LaserSerial
from django.shortcuts import get_object_or_404
from .forms import ReviewForm, racketform, CheckoutForm


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
            # Assign a default user (anonymous) — user auth not set up yet
            from django.contrib.auth.models import User
            anon, _ = User.objects.get_or_create(username='guest')
            new_review.user = anon
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


def checkout(request, racket_id):
    racket = get_object_or_404(rackets, id=racket_id)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return render(request, 'DBL/order_confirm.html', {
                'racket': racket,
                'order': form.cleaned_data,
            })
    else:
        form = CheckoutForm()
    return render(request, 'DBL/checkout.html', {'racket': racket, 'form': form})

from django import forms
from .models import rackets, racket_type, racket_reviews


class racketform(forms.Form):
    racket_type = forms.ModelChoiceField(queryset=racket_type.objects.all(), label='Select Type')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = racket_reviews
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"⭐ {i}") for i in range(1, 6)], attrs={
                'class': 'w-full bg-[#11141d] border border-gray-800 rounded-xl px-4 py-2.5 text-sm text-gray-200 outline-none focus:border-orange-500 transition'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'w-full bg-[#11141d] border border-gray-800 rounded-xl px-4 py-2.5 text-sm text-gray-200 outline-none focus:border-orange-500 transition h-24 resize-none',
                'placeholder': 'Share your experience with this racket...'
            }),
        }


class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name', 'class': 'checkout-input'
    }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number', 'class': 'checkout-input'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address', 'class': 'checkout-input'
    }))
    address_line1 = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Address Line 1', 'class': 'checkout-input'
    }))
    address_line2 = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Address Line 2 (Optional)', 'class': 'checkout-input'
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'City', 'class': 'checkout-input'
    }))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'State', 'class': 'checkout-input'
    }))
    pincode = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
        'placeholder': 'PIN Code', 'class': 'checkout-input'
    }))
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('upi', 'UPI'),
        ('card', 'Credit / Debit Card'),
    ]
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)

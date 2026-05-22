from django import forms
from .models import rackets, racket_type, racket_reviews, LaserSerial, racket_reviews


class racketform(forms.Form):
    racket_type = forms.ModelChoiceField(queryset=racket_type.objects.all(), label='Select Brand')
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = racket_reviews
        fields = ['user', 'rating', 'comment']
        # Adding Tailwind CSS styles directly to the form fields
        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'w-full bg-[#11141d] border border-gray-800 rounded-xl px-4 py-2.5 text-sm text-gray-200 outline-none focus:border-orange-500 transition',
                'placeholder': 'Enter your name'
            }),
            'rating': forms.Select(choices=[(i, f"⭐ {i}") for i in range(1, 6)], attrs={
                'class': 'w-full bg-[#11141d] border border-gray-800 rounded-xl px-4 py-2.5 text-sm text-gray-200 outline-none focus:border-orange-500 transition'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'w-full bg-[#11141d] border border-gray-800 rounded-xl px-4 py-2.5 text-sm text-gray-200 outline-none focus:border-orange-500 transition h-24 resize-none',
                'placeholder': 'Share your experience with this racket...'
            }),
        }
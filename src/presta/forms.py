from django import forms
from .models import Presta
import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]


class PrestaForm(forms.ModelForm):
    class Meta:
        model = Presta
        exclude = ('pub_date',)
        widgets = {
            'presta_name': forms.TextInput(attrs={'class': 'form-control'}),
            'presta_date': forms.DateInput(format=('%d %b, %Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'presta_start': forms.Select(choices=HOUR_CHOICES),
            'presta_end': forms.Select(choices=HOUR_CHOICES),
        }
        help_texts = {
            'presta_comments': ' (Genres Musicales souhaitées, Lien de Playlist, etc.)', }


'''
class PrestaForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    date_presta = forms.DateTimeField(label='Date')
'''


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

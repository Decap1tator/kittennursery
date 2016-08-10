from django import forms

from .models import Kitten

class KittenForm(forms.ModelForm):
    BATHROOM_TYPES = (
        ('urine','urine'),
        ('bm','bowel movement'),
        ('none','none'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    pre_feed = forms.IntegerField()
    post_feed = forms.IntegerField()
    bathroom = forms.CharField()
    #bathroom = forms.CharField(widget=forms.Select(choices=BATHROOM_TYPES))

    class Meta:
        model = Kitten
        fields = ('name','pre_feed','post_feed','bathroom')
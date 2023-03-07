
from django import forms
from .models import Attributes

class AttributesForm(forms.ModelForm):

    class Meta:
        model = Attributes

        fields = ['noun', 'noun2', 'verb', 'verb2', 'adjective', 'adjective2', 'item', 'place', 'animal']

from .models import vuses
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput

class chatForm(ModelForm):
    class Meta:
        model = vuses
        fields = ["title", "structure"]
        widjets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Title'
            }
            ),
            "structure" : {}

        }
from django import forms
from calculator.models import Profile


class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)

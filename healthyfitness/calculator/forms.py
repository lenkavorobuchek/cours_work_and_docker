
from .models import Calculator
from django.forms import ModelForm, TextInput


class CalculatorForm(ModelForm):
    class Meta:
        model = Calculator
        fields = ["age", "weight", "growth", "gender", "user_aim", "user_activity"]
        widgets = {
            'age': TextInput(attrs={'placeholder': 'Укажите возраст'}),
            'weight': TextInput(attrs={'placeholder': 'Укажите вес'}),
            'growth': TextInput(attrs={'placeholder': 'Укажите рост'}),
        }


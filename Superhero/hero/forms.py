from django import forms
 
class HeroForm(forms.Form):
    name = forms.CharField(max_length=100)
    alias = forms.CharField(max_length=200)
    strength = forms.CharField(max_length=200)
    weakness = forms.CharField(max_length=200)
    description = forms.Textarea()
    photo = forms.ImageField()
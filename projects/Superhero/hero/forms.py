from django import forms
 
class HeroForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    img_field = forms.ImageField()
from django import forms

class formSintomas(forms.Form):
    temperatura = forms.FloatField()
    dolorGarganta = forms.IntegerField(max_value=5,min_value=0)
    tos = forms.IntegerField(max_value=5,min_value=0)
    senGusto = forms.IntegerField(max_value=5,min_value=0)
    senOlfato = forms.IntegerField(max_value=5,min_value=0)
    respiracion = forms.IntegerField(max_value=5,min_value=0)
    
    
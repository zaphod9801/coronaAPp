from django import forms
opciones = (
    ('Si','Si'),
    ('No','No'),
)

class formSintomas(forms.Form):
    temperatura = forms.FloatField(label='Temperatura')
    dolorGarganta = forms.IntegerField(label='Dolor de garganta',max_value=5,min_value=0)
    tos = forms.IntegerField(label='Tos',max_value=5,min_value=0)
    senGusto = forms.ChoiceField(label='Sentido del gusto', widget=forms.Select, choices=opciones)
    senOlfato = forms.ChoiceField(label='Sentido del olfato', widget=forms.Select, choices=opciones)
    respiracion = forms.IntegerField(label='Respiracion',max_value=5,min_value=0)
    dolorPecho = forms.IntegerField(label='Dolor Pecho',max_value=5,min_value=0)
    
    
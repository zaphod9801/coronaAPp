from django import forms
opciones = (
    ('Si','Si'),
    ('No','No'),
)

class formSintomas(forms.Form):
    temperatura = forms.FloatField(label='Temperatura (en grados centigrados)')
    dolorGarganta = forms.IntegerField(label='Dolor de garganta (0 a 5)',max_value=5,min_value=0)
    tos = forms.IntegerField(label='Tos (0 a 5)',max_value=5,min_value=0)
    senGusto = forms.ChoiceField(label='Tiene sentido del gusto?', widget=forms.Select, choices=opciones)
    senOlfato = forms.ChoiceField(label='Tiene sentido del olfato?', widget=forms.Select, choices=opciones)
    respiracion = forms.IntegerField(label='Dificultad para respirar (0 a 5)',max_value=5,min_value=0)
    dolorPecho = forms.IntegerField(label='Dolor en el pecho (0 a 5)',max_value=5,min_value=0)
    
    